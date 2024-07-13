from core.g_var import Config
from colorama import init as fore_init

import json

def readConfig():
    Config.config=json.loads(open("./config.json","r").read())

def init():
    readConfig()
    fore_init()