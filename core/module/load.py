import importlib  
import os

from core.module.Event.Events import Event
from core.module.log import log
from core.g_var import Event as g_var_e

class load:
    def load():
        # 写eventMap
        for name, value in Event.__dict__.items():
            if(isinstance(value,type)):
                g_var_e.eventMap[value]=[]
        # 遍历插件文件夹
        for filename in os.listdir(os.path.join('./plugins')):
            try:
                # 识别是否是插件
                if(os.path.isfile("./plugins/"+filename+"/plugin.py")):
                    module=importlib.import_module(f"plugins.{filename}.plugin")
                    module.Plugin.onEnable()
                    log.info("已加载插件 "+filename)
                else:
                    log.warn("无法加载插件 "+filename)
            except:
                log.warn("无法加载插件 "+filename)