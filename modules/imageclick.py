import pyautogui
import time
import sys
from datetime import datetime
from pydoc import importfile
from colorama import init, Fore, Style

init(convert=True)

time_print = importfile('./modules/timeprint.py')

def image_click(name, image, next_time=2, waite_time=2): # 4s + parametro
  count = 1

  print(Fore.WHITE + Style.BRIGHT + datetime.now().strftime('%d/%m %H:%M:%S'), Fore.BLUE + Style.BRIGHT + 'WARNING: Search ' + name)
  print(Fore.WHITE + Style.BRIGHT + datetime.now().strftime('%d/%m %H:%M:%S'), Fore.CYAN + Style.BRIGHT + 'WARNING: Waiting 5 seconds')
  time.sleep(4)
  locateButtons = list(pyautogui.locateAllOnScreen(image, confidence=0.9))
  time.sleep(1)

  if (locateButtons):
    print(Fore.WHITE + Style.BRIGHT + datetime.now().strftime('%d/%m %H:%M:%S'), Fore.GREEN + Style.BRIGHT + 'SUCCESS: ' + str(len(locateButtons)) + ' Buttons found')
    for position in locateButtons:
      time_print(waite_time)
      pyautogui.moveTo(position)
      pyautogui.click(position)
      print(Fore.WHITE + Style.BRIGHT + datetime.now().strftime('%d/%m %H:%M:%S'), Fore.MAGENTA + Style.BRIGHT + 'WARNING: Button '+ str(count) +' pressed')
      count += 1
  else:
    print(Fore.WHITE + Style.BRIGHT + datetime.now().strftime('%d/%m %H:%M:%S'), Fore.RED + Style.BRIGHT + 'ERROR: ' + name + ' NOT FOUND')

  time_print(next_time)

sys.modules[__name__] = image_click