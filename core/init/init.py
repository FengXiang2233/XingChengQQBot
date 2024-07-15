from core.g_var import Config
from colorama import init as fore_init

import os
import json

def init():
    Config.config=json.loads(open("./config.json","r").read())
    if not os.path.isdir("./plugins"):
        os.mkdir("plugins")
    fore_init()