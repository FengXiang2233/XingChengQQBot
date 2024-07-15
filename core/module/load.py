import importlib  
import os

from core.module.log import log

class load:
    def load():
        # 遍历插件文件夹
        for filename in os.listdir(os.path.join('./plugins')):
            try:
                # 识别是否是插件
                if(os.path.isfile("./plugins/"+filename+"/plugin.py")):
                    module=importlib.import_module(f"plugins.{filename}.plugin")
                    module.Plugin.onEnable()
                else:
                    log.warn("无法加载插件 "+filename)
            except:
                log.warn("无法加载插件 "+filename)