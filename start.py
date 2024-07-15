from core.init.init import init
from core.module.load import load
from core.module.console import Console

init()
load.load()
while True:
    Console().analytic(input("> "))