from core.init.init import init
from core.network.QQApi import QQApi
from core.module.console import Console

init()
while True:
    Console().analytic(input("> "))