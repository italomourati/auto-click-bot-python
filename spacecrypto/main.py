import time
from pydoc import importfile
import pyautogui

image_click = importfile('./modules/imageclick.py')
time_print = importfile('./modules/timeprint.py')

WAIT_TIME_LAUNCH = 50
WAIT_TIME_WALLET = 20
WAIT_TIME_SHIP = 10
WAIT_TIME_CLOSE_GAME = 900 # 15m

CONNECT_WALLET_BTS = './spacecrypto/assets/connect_wallet_bt.PNG'
ICON_SPACE_BTS = './spacecrypto/assets/icon_space_bt.PNG'
PLAY_BTS = './spacecrypto/assets/play_bt.PNG'
SIGN_META_MASK_BTS = './spacecrypto/assets/sign_meta_mask_bt.PNG'
CONFIRM_BTS = './spacecrypto/assets/confirm_bt.PNG'
FIGHT_BOSS_BTS = './spacecrypto/assets/fight_boss_bt.PNG'
SHIP_FIGHT_BTS = './spacecrypto/assets/ship_fight_bt.PNG'
ICON_TAB_BTS = './spacecrypto/assets/icon_tab_bt.PNG'

def launch_space_crypto(): # 2m 8s
  image_click('Icon Space', ICON_SPACE_BTS, WAIT_TIME_LAUNCH) # 57s
  image_click('Connect Wallet', CONNECT_WALLET_BTS, WAIT_TIME_WALLET) # 27s
  image_click('Sign Meta Mask', SIGN_META_MASK_BTS, WAIT_TIME_WALLET) # 27s
  image_click('Play', PLAY_BTS, WAIT_TIME_SHIP) # 17s

def play_ship_space(): # 1m 16s
  for ship in range(4): # 44s
    image_click('Ship Fight', SHIP_FIGHT_BTS) # 11s
  image_click('Ship Fight', SHIP_FIGHT_BTS) # 11s
  image_click('Ship Fight', SHIP_FIGHT_BTS) # 7s
  image_click('Fight Boss', FIGHT_BOSS_BTS) # 7s
  image_click('Confirm', CONFIRM_BTS) # 7s

def close_space_game(): # 13s
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

def play_bot_space():
  launch_space_crypto() 
  play_ship_space() 
  time_print(WAIT_TIME_CLOSE_GAME) 
  close_space_game() 