import pyautogui
import time
import sys
from datetime import datetime
from pydoc import importfile
from colorama import init, Fore, Style

init(convert=True)

time_print = importfile('./modules/timeprint.py')

def image_one_click(name, image, next_time=2, waite_time=2): # 4s + parametro
  dataNow = datetime.now().strftime('%H:%M:%S')
  print(Fore.WHITE + Style.BRIGHT + f'{dataNow}' + Fore.BLUE + Style.BRIGHT + f' WARNING: Search {name}')
  print(Fore.WHITE + Style.BRIGHT + f'{dataNow}' + Fore.CYAN + Style.BRIGHT + ' WARNING: Waiting 5 seconds')
  time.sleep(4)
  locateButton = pyautogui.locateOnScreen(image, confidence=0.9)
  time.sleep(1)

  if (locateButton):
    print(Fore.WHITE + Style.BRIGHT + f'{dataNow}' + Fore.GREEN + Style.BRIGHT + ' SUCCESS: 1 Buttons found')
    time_print(waite_time)
    pyautogui.moveTo(locateButton)
    pyautogui.click(locateButton)
    print(Fore.WHITE + Style.BRIGHT + f'{dataNow}' + Fore.MAGENTA + Style.BRIGHT + ' WARNING: Button pressed')
  else:
    print(Fore.WHITE + Style.BRIGHT + f'{dataNow}' + Fore.RED + Style.BRIGHT + f' ERROR: {name} NOT FOUND')

  time_print(next_time)

sys.modules[__name__] = image_one_click