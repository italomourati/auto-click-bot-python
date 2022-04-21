from lib2to3.pytree import convert
import time
import sys
from datetime import datetime
from colorama import init, Fore, Style

init(convert=True)

def time_print(seconds):
  dataNow = datetime.now().strftime('%H:%M:%S')
  print(Fore.WHITE + Style.BRIGHT + f'{dataNow}' + Fore.CYAN + Style.BRIGHT + f' WARNING: Waiting {seconds} seconds')
  time.sleep(seconds) 


sys.modules[__name__] = time_print