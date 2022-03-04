import time
from pydoc import importfile

image_click = importfile('./modules/imageclick.py')
time_print = importfile('./modules/timeprint.py')

WAIT_ALL_HEROS = 10
WAIT_CONNECT_TIME = 15
WAIT_TIME_PROCESS = 120

BACK_BTS = './bombcrypto/assets/back_bt.PNG'
HUNTING_BTS = './bombcrypto/assets/hunting_bt.PNG'
TRUNK_BTS = './bombcrypto/assets/trunk_bt.PNG'
CLOSE_TRUNK_BT = './bombcrypto/assets/close_trunk_bt.PNG'
HEROS_BTS = './bombcrypto/assets/heros_bt.PNG'
ALL_HEROS_BTS = './bombcrypto/assets/all_heros_bt.PNG'
CLOSE_HEROS_BTS = './bombcrypto/assets/close_heros_bt.PNG'
CONNECT_META_MASK_BTS = './bombcrypto/assets/connect_meta_mask_bt.PNG'
CONNECT_WALLET_BTS = './bombcrypto/assets/connect_wallet_bt.PNG'
SIGN_META_MASK_BTS = './bombcrypto/assets/sign_meta_mask_bt.PNG'
WRONG_NETWORK_BTS = './bombcrypto/assets/wrong_network_bt.PNG'

def refresh_heros(): # 22s
  image_click('Back', BACK_BTS) # 11s
  image_click('Hunting', HUNTING_BTS) # 11s

def open_and_close_trunk(): # 22s
  image_click('Trunk', TRUNK_BTS) # 11s
  image_click('Close Trunk', CLOSE_TRUNK_BT) # 11s

def play_heros(): # 1m 5s
  image_click('Back', BACK_BTS) # 11s
  image_click('Heros', HEROS_BTS, WAIT_ALL_HEROS) # 21s
  image_click('All Heros', ALL_HEROS_BTS) # 11s
  image_click('Close', CLOSE_HEROS_BTS) # 11s
  image_click('Hunting', HUNTING_BTS) # 11s

def connect_bomb(): # 1m 45s
  image_click('Wrong Network', WRONG_NETWORK_BTS, WAIT_CONNECT_TIME) # 26s
  image_click('Connect Wallet', CONNECT_WALLET_BTS, WAIT_ALL_HEROS) # 21s
  image_click('Connect Meta Mask', CONNECT_META_MASK_BTS, WAIT_ALL_HEROS) # 21s
  image_click('Sign Meta Mask', SIGN_META_MASK_BTS, WAIT_CONNECT_TIME) # 26s
  image_click('Hunting', HUNTING_BTS) # 11s

def play_bot_bomb(): 
  connect_bomb() 
  play_heros() 
  time_print(WAIT_TIME_PROCESS) 

  for item in range(5): 
    refresh_heros() 
    time_print(WAIT_TIME_PROCESS) 
    open_and_close_trunk() 
    time_print(WAIT_TIME_PROCESS) 
