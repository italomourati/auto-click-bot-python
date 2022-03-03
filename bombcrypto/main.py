import time
from pydoc import importfile

image_click = importfile('./modules/imageclick.py')

WAIT_TIME = 2
WAIT_ALL_HEROS = 10
WAIT_TIME_PROCESS = 120

BACK_BTS = './bombcrypto/assets/back_bt.PNG'
HUNTING_BTS = './bombcrypto/assets/hunting_bt.PNG'
TRUNK_BTS = './bombcrypto/assets/trunk_bt.PNG'
CLOSE_TRUNK_BT = './bombcrypto/assets/close_trunk_bt.PNG'
HEROS_BTS = './bombcrypto/assets/heros_bt.PNG'
ALL_HEROS_BTS = './bombcrypto/assets/all_heros_bt.PNG'
CLOSE_HEROS_BTS = './bombcrypto/assets/close_heros_bt.PNG'

def refresh_heros():
  image_click('Back Button', BACK_BTS, WAIT_TIME)
  image_click('Hunting Button', HUNTING_BTS, WAIT_TIME)

def open_and_close_trunk():
  image_click('Trunk Button', TRUNK_BTS, WAIT_TIME)
  image_click('Close Trunk Button', CLOSE_TRUNK_BT, WAIT_TIME)

def play_heros():
  image_click('Back Button', BACK_BTS, WAIT_TIME)
  image_click('Heros Button', HEROS_BTS, WAIT_TIME)
  time.sleep(WAIT_ALL_HEROS)
  image_click('All Heros Button', ALL_HEROS_BTS, WAIT_TIME)
  image_click('Close Button', CLOSE_HEROS_BTS, WAIT_TIME)
  image_click('Hunting Button', HUNTING_BTS, WAIT_TIME)

def play_bot_bomb(): # 27m 6s
  play_heros() # 2m 26s
  time.sleep(WAIT_TIME_PROCESS) # 2m

  for item in range(5): # 22m  40s
    refresh_heros() # 16s
    time.sleep(WAIT_TIME_PROCESS) # 2m
    open_and_close_trunk() # 16s
    time.sleep(WAIT_TIME_PROCESS) # 2m