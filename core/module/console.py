from core.module.log import log
from core.network.QQApi import QQApi

class Console:

    qq_api = QQApi()

    cmd={
        "exit":exit,
        "login":qq_api.login
    }

    def analytic(self,command:str):
        cmd=command.split(" ")
        try:
            self.cmd[cmd[0]](*(cmd[1:]))
        except IndexError:
            log.warn("指令不存在")
        except KeyError:
            log.warn("指令不存在")