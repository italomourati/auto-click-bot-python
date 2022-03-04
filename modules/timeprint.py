from lib2to3.pytree import convert
import time
import sys
from datetime import datetime
from colorama import init, Fore, Style

init(convert=True)

def time_print(seconds):
  print(Fore.WHITE + Style.BRIGHT + datetime.now().strftime('%d/%m %H:%M:%S'), Fore.CYAN + Style.BRIGHT + 'WARNING: Waiting ' + str(seconds) + ' seconds')
  time.sleep(seconds) 


sys.modules[__name__] = time_print