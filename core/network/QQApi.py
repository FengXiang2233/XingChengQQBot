import time
import json
import requests
import websocket
import threading

from core.module.log import log
from core.g_var import Event as g_var_e
from core.module.Event.EventGroups import EventGroup

class QQApi:

    appId:str
    sessionId:str
    clientSecret:str
    appAccessToken:dict

    qq_api="https://api.sgroup.qq.com"
    requestHeaders:dict

    eventGroupsMap:dict={}

    def login(self,appId:str,clientSecret:str):
        self.appId=appId
        self.clientSecret=clientSecret
        self.appAccessToken=self.getAppAccessToken(appId,clientSecret)
        self.requestHeaders={
            "Authorization": "QQBot "+self.appAccessToken["access_token"],
            "X-Union-Appid": self.appId
        }
        # ws线程
        threading.Thread(target=QQWebSocket().connect,args=(self.getWebSocketAddress(),self)).start()
        # AppAccessToken更新线程
        threading.Thread(target=self.updateAppAccessToken).start()

    def getAppAccessToken(self,appId:str,clientSecret:str)->dict:
        appAccessToken:dict=requests.post("https://bots.qq.com/app/getAppAccessToken",json={
            "appId": appId,
            "clientSecret": clientSecret
        }).json()
        print(appAccessToken)
        return appAccessToken

    def updateAppAccessToken(self):
        while True:
            time.sleep(float(self.appAccessToken["expires_in"])-40)
            self.appAccessToken=self.getAppAccessToken(self.appId,self.clientSecret)
            self.requestHeaders={
                "Authorization": "QQBot "+self.appAccessToken["access_token"],
                "X-Union-Appid": self.appId
            }
            log.debug("AppAccessToken已更新")

    def getWebSocketAddress(self)->str:
        return requests.get(self.qq_api+"/gateway",headers=self.requestHeaders).json()["url"]

    def getPluginRegisterEvent(self):
        # 写eventGroupsMap
        self.eventGroupsMap:dict={}
        for name, value in EventGroup.__dict__.items():
            if(isinstance(value,type)):
                self.eventGroupsMap[value]=0
        for e in g_var_e.eventMap.keys():
            self.eventGroupsMap[e.group]+=1
    
    def sendGroupMessages(self,group_openid,msg,re_msg_id,msg_type=0):
        print(requests.post(
            url=self.qq_api+"/v2/groups/"+group_openid+"/messages",
            headers=self.requestHeaders,
            json={
                "msg_type": msg_type,
                "content": msg,
                "msg_id": re_msg_id
            }
        ).json())


class QQWebSocket:

    wsObj:websocket.WebSocketApp
    
    def connect(self,address:str,apiObj:QQApi):
        self.qq_api=apiObj
        self.wsObj=websocket.WebSocketApp(address,
                               on_message=self.recv,
                               on_close=self.recl)
        self.Message=QQMessage(apiObj,self.wsObj)
        self.wsObj.run_forever()

    def recv(self,wsObj, message):
        msg=json.loads(message)
        self.Message.message(msg)

    def recl(self,wsObj):
        pass

class QQMessage:

    new_s:int=None

    def __init__(self,apiObj,wsObj):
        self.qq_api:QQApi=apiObj
        self.wsObj:websocket.WebSocketApp=wsObj

    def message(self,msg:dict):
        op_table={
            0: self.Dispatch,
            10: self.Hello,
            11: self.HeartbeatACK,
        }
        op_table[msg["op"]](msg)

    def ack(self,htime):
        while True:
            time.sleep(htime)
            try:
                self.wsObj.send(json.dumps(
                    {
                        "op": 1,
                        "d": self.new_s
                    }
                ))
            # 断线重连
            except websocket._exceptions.WebSocketConnectionClosedException:
                log.error("ws通讯断开正在尝试恢复")
                self.wsObj.run_forever()
                self.wsObj.send(json.dumps(
                    {
                        "op": 6,
                        "d": {
                            "token": "QQBot "+self.qq_api.appAccessToken["access_token"],
                            "session_id": self.qq_api.sessionId,
                            "seq": self.new_s
                        }
                    }
                ))
            log.debug("已发送心跳包")

    # op 0
    def Dispatch(self,msg:dict):
        # session会话事件
        if(msg["t"]=="READY"):
            self.qq_api.sessionId=msg["d"]["session_id"]
        # 群at事件
        elif(msg["t"]=="GROUP_AT_MESSAGE_CREATE"):
            self.qq_api.sendGroupMessages(
                group_openid=msg["d"]["group_openid"],
                msg="橘子是猫娘！",
                re_msg_id=msg["d"]["id"]
            )
        # debug
        print(msg)

    # op 10
    def Hello(self,msg:dict):
        # 心跳包线程
        threading.Thread(target=self.ack,args=[msg["d"]["heartbeat_interval"]/1000.0000]).start()
        self.qq_api.getPluginRegisterEvent()
        intents=0
        for e in self.qq_api.eventGroupsMap.keys():
            if self.qq_api.eventGroupsMap[e] > 0:
                intents=intents|e.id
        # 注册session会话
        self.wsObj.send(json.dumps(
            {
                "op": 2,
                "d": {
                    "token": "QQBot "+self.qq_api.appAccessToken["access_token"],
                    "shard": [0,1],
                    "intents": intents
                }
            }
        ))

    # op 11
    def HeartbeatACK(self,msg:dict):
        log.debug("心跳包已返回")