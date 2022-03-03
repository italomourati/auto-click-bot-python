import pyautogui
import time
import sys

def image_click(name, image, waite_time): # 4s + parametro
  count = 1

  print('Search [' + name + ']')
  time.sleep(2)
  locateButtons = list(pyautogui.locateAllOnScreen(image, confidence=0.9))
  time.sleep(2)

  if (locateButtons):
    print('SUCCESS: [' + str(len(locateButtons)) + '] Buttons found')
    for position in locateButtons:
      time.sleep(waite_time)
      pyautogui.moveTo(position)
      pyautogui.click(position)
      print('Button ['+ str(count) +'] pressed')
      count += 1
  else:
    print('ERROR: [' + name + '] not found')

sys.modules[__name__] = image_click