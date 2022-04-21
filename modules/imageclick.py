import pyautogui
import time
import sys
from datetime import datetime
from pydoc import importfile
from colorama import init, Fore, Style

init(convert=True)

time_print = importfile('./modules/timeprint.py')

def image_click(name, image, next_time=2, waite_time=2, bomb=False): # 4s + parametro
  count = 1
  dataNow = datetime.now().strftime('%H:%M:%S')
  print(Fore.WHITE + Style.BRIGHT + f'{dataNow}' + Fore.BLUE + Style.BRIGHT + f' WARNING: Search {name}')
  print(Fore.WHITE + Style.BRIGHT + f'{dataNow}' + Fore.CYAN + Style.BRIGHT + ' WARNING: Waiting 5 seconds')
  time.sleep(4)
  locateButtons = list(pyautogui.locateAllOnScreen(image, confidence=0.9))
  time.sleep(1)

  if (locateButtons):
    print(Fore.WHITE + Style.BRIGHT + f'{dataNow}' + Fore.GREEN + Style.BRIGHT + f' SUCCESS: {len(locateButtons)} Buttons found')
    for position in locateButtons:
      time_print(waite_time)
      if bomb:
        x = position.left
        y = position.top
        pyautogui.moveTo(x+80,y)
        pyautogui.click(x+80,y)
      else:
        pyautogui.moveTo(position)
        pyautogui.click(position)
      print(Fore.WHITE + Style.BRIGHT + f'{dataNow}' + Fore.MAGENTA + Style.BRIGHT + f' WARNING: Button {count} pressed')
      count += 1
  else:
    print(Fore.WHITE + Style.BRIGHT + f'{dataNow}' + Fore.RED + Style.BRIGHT + f' ERROR: {name} NOT FOUND')

  time_print(next_time)

sys.modules[__name__] = image_click