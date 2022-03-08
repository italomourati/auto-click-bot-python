import time
from pydoc import importfile
import pyautogui

image_click = importfile('./modules/imageclick.py')
time_print = importfile('./modules/timeprint.py')

WAIT_TIME_LAUNCH = 50
WAIT_TIME_WALLET = 10
WAIT_TIME_ROD = 5
WAIT_TIME_CLOSE_GAME = 900 # 15m

CONNECT_WALLET_BTS = './fishcrypto/assets/connect_wallet_bt.PNG'
ICON_FISH_BTS = './fishcrypto/assets/icon_fish_bt.PNG'
SIGN_META_MASK_BTS = './fishcrypto/assets/sign_meta_mask_bt.PNG'
ADD_ROD_1_BTS = './fishcrypto/assets/add_rod_1_bt.PNG'
ADD_ROD_2_BTS = './fishcrypto/assets/add_rod_2_bt.PNG'
ADD_ROD_3_BTS = './fishcrypto/assets/add_rod_3_bt.PNG'
ROD_1_BTS = './fishcrypto/assets/rod_1_bt.PNG'
ROD_2_BTS = './fishcrypto/assets/rod_2_bt.PNG'
ROD_3_BTS = './fishcrypto/assets/rod_3_bt.PNG'
PICK_ROD_BTS = './fishcrypto/assets/pick_rod_bt.PNG'
PICK_ROD_FRIEND_BTS = './fishcrypto/assets/pick_rod_friend_bt.PNG'
ADD_FRIEND_ROD_1_BTS = './fishcrypto/assets/add_friend_rod_1_bt.PNG'
FRIEND_1_BTS = './fishcrypto/assets/friend_1_bt.PNG'
ROD_FRIEND_1_BTS = './fishcrypto/assets/rod_friend_1_bt.PNG'
ICON_TAB_BTS = './fishcrypto/assets/icon_tab_bt.PNG'

def launch_fish_crypto(): # 1m 31s
  image_click('Icon Fish', ICON_FISH_BTS, WAIT_TIME_LAUNCH) # 57s
  image_click('Connect Wallet', CONNECT_WALLET_BTS, WAIT_TIME_WALLET) # 17s
  image_click('Sign Meta Mask', SIGN_META_MASK_BTS, WAIT_TIME_WALLET) # 17s

def pick_rod_player(): # 2m 3s
  image_click('Add Rod 3', ADD_ROD_3_BTS, WAIT_TIME_WALLET) # 17s
  image_click('Select Rod 3', ROD_3_BTS, WAIT_TIME_ROD) # 12s
  image_click('Pick Rod', PICK_ROD_BTS, WAIT_TIME_ROD) # 12s
  image_click('Add Rod 2', ADD_ROD_2_BTS, WAIT_TIME_WALLET) # 17s
  image_click('Select Rod 2', ROD_2_BTS, WAIT_TIME_ROD) # 12s
  image_click('Pick Rod', PICK_ROD_BTS, WAIT_TIME_ROD) # 12s
  image_click('Add Rod 1', ADD_ROD_1_BTS, WAIT_TIME_WALLET) # 17s
  image_click('Select Rod 1', ROD_1_BTS, WAIT_TIME_ROD) # 12s
  image_click('Pick Rod', PICK_ROD_BTS, WAIT_TIME_ROD) # 12s

def pick_rod_friend(): # 58s
  image_click('Add Friend Rod 1', ADD_FRIEND_ROD_1_BTS, WAIT_TIME_WALLET) # 17s
  image_click('Select Friend 1', FRIEND_1_BTS, WAIT_TIME_WALLET) # 17s
  image_click('Select Rod 1', ROD_FRIEND_1_BTS, WAIT_TIME_ROD) # 12s
  image_click('Pick Rod', PICK_ROD_FRIEND_BTS, WAIT_TIME_ROD) # 12s

def close_fish_game(): # 13s
  image_click('Icon Tab', ICON_TAB_BTS)
  time.sleep(2)
  pyautogui.keyDown('ctrl')
  pyautogui.press('t')
  pyautogui.keyUp('ctrl')
  time.sleep(2)
  pyautogui.keyDown('ctrl')
  pyautogui.press('1')
  pyautogui.keyUp('ctrl')
  time.sleep(2)
  pyautogui.keyDown('ctrl')
  pyautogui.press('w')
  pyautogui.keyUp('ctrl')

def play_bot_fish():
  launch_fish_crypto()
  pick_rod_player()
  pick_rod_friend()
  close_fish_game()