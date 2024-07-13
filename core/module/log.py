from colorama import Fore as fore_color

import time

class log:
    # 用于获取时间的函数
    def _time():
        # 获取当前时间
        time_str = time.strftime("%H:%M:%S")
        return time_str

    def log(text):
        print(text)

    def info(text):
        text = f'[info {log._time()}] '+str(text)
        log.log(text)

    def warn(text):
        text = f'{fore_color.YELLOW}[warn {log._time()}] '+str(text)+fore_color.WHITE
        log.log(text)

    def error(text):
        text = f'{fore_color.RED}[error {log._time()}] '+str(text)+fore_color.WHITE
        log.log(text)

    def debug(text):
        text = f'{fore_color.BLUE}[debug {log._time()}] '+str(text)+fore_color.WHITE
        log.log(text)
