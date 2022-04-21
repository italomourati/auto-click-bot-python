from pydoc import importfile
from re import T
import pyautogui
import time
from datetime import datetime
from colorama import init, Fore, Style

init(convert=True)

image_click = importfile('./modules/imageclick.py')
image_one_click = importfile('./modules/imageoneclick.py')

WAIT_TIME_LAUNCH = 50
WAIT_TIME_WALLET = 20
WAIT_HUNTING_BOSS = 5
WAIT_START_BOSS = 10
WAIT_FIGTH_BOSS = 50

ICON_REFRESH_BTS = './lunarush/assets/icon_refresh_bt.PNG'
CONNECT_WALLET_BTS = './lunarush/assets/connect_meta_mask_bt.PNG'
CONNECT_WALLET_2_BTS = './lunarush/assets/connect_meta_mask_2_bt.PNG'
SIGN_META_MASK_BTS = './lunarush/assets/sign_meta_mask_bt.PNG'
HUNTING_BOSS_BTS = './lunarush/assets/hunting_boss_bt.PNG'
LEVEL_BOSS_SELECT_BTS = './lunarush/assets/level_boss_bt.PNG'
EXPAND_WARRIORS_BTS = './lunarush/assets/expand_warriors_bt.PNG'
SCROLL_HEROS_1 = './lunarush/assets/scroll_heros_1.PNG'
SCROLL_HEROS_2 = './lunarush/assets/scroll_heros_2.PNG'
TOPO_BT = './lunarush/assets/topo_bt.PNG'
DELETE_ALL = './lunarush/assets/delete_all_bt.PNG'

WS1 = './lunarush/assets/warriors/select/1.PNG'
WS2 = './lunarush/assets/warriors/select/2.PNG'
WS3 = './lunarush/assets/warriors/select/3.PNG'
WS4 = './lunarush/assets/warriors/select/4.PNG'
WS5 = './lunarush/assets/warriors/select/5.PNG'
WS6 = './lunarush/assets/warriors/select/6.PNG'
WS7 = './lunarush/assets/warriors/select/7.PNG'
WS8 = './lunarush/assets/warriors/select/8.PNG'
WS9 = './lunarush/assets/warriors/select/9.PNG'
WS10 = './lunarush/assets/warriors/select/10.PNG'
WS11 = './lunarush/assets/warriors/select/11.PNG'
WS12 = './lunarush/assets/warriors/select/12.PNG'
WS13 = './lunarush/assets/warriors/select/13.PNG'
WS14 = './lunarush/assets/warriors/select/14.PNG'
WS15 = './lunarush/assets/warriors/select/15.PNG'

WS1_1 = './lunarush/assets/warriors/select/1_1.PNG'
WS2_1 = './lunarush/assets/warriors/select/2_1.PNG'
WS3_1 = './lunarush/assets/warriors/select/3_1.PNG'
WS4_1 = './lunarush/assets/warriors/select/4_1.PNG'
WS5_1 = './lunarush/assets/warriors/select/5_1.PNG'
WS6_1 = './lunarush/assets/warriors/select/6_1.PNG'
WS7_1 = './lunarush/assets/warriors/select/7_1.PNG'
WS8_1 = './lunarush/assets/warriors/select/8_1.PNG'
WS9_1 = './lunarush/assets/warriors/select/9_1.PNG'
WS10_1= './lunarush/assets/warriors/select/10_1.PNG'
WS11_1 = './lunarush/assets/warriors/select/11_1.PNG'
WS12_1= './lunarush/assets/warriors/select/12_1.PNG'
WS13_1 = './lunarush/assets/warriors/select/13_1.PNG'
WS14_1= './lunarush/assets/warriors/select/14_1.PNG'
WS15_1= './lunarush/assets/warriors/select/15_1.PNG'

WD1 = './lunarush/assets/warriors/deselect/1.PNG'
WD2 = './lunarush/assets/warriors/deselect/2.PNG'
WD3 = './lunarush/assets/warriors/deselect/3.PNG'
WD4 = './lunarush/assets/warriors/deselect/4.PNG'
WD5 = './lunarush/assets/warriors/deselect/5.PNG'
WD6 = './lunarush/assets/warriors/deselect/6.PNG'
WD7 = './lunarush/assets/warriors/deselect/7.PNG'
WD8 = './lunarush/assets/warriors/deselect/8.PNG'
WD9 = './lunarush/assets/warriors/deselect/9.PNG'
WD10 = './lunarush/assets/warriors/deselect/10.PNG'
WD11 = './lunarush/assets/warriors/deselect/11.PNG'
WD12 = './lunarush/assets/warriors/deselect/12.PNG'
WD13 = './lunarush/assets/warriors/deselect/13.PNG'
WD14 = './lunarush/assets/warriors/deselect/14.PNG'
WD15 = './lunarush/assets/warriors/deselect/15.PNG'

WD1_1 = './lunarush/assets/warriors/deselect/1_1.PNG'
WD2_1 = './lunarush/assets/warriors/deselect/2_1.PNG'
WD3_1 = './lunarush/assets/warriors/deselect/3_1.PNG'
WD4_1 = './lunarush/assets/warriors/deselect/4_1.PNG'
WD5_1 = './lunarush/assets/warriors/deselect/5_1.PNG'
WD6_1 = './lunarush/assets/warriors/deselect/6_1.PNG'
WD7_1 = './lunarush/assets/warriors/deselect/7_1.PNG'
WD8_1 = './lunarush/assets/warriors/deselect/8_1.PNG'
WD9_1 = './lunarush/assets/warriors/deselect/9_1.PNG'
WD10_1= './lunarush/assets/warriors/deselect/10_1.PNG'
WD11_1 = './lunarush/assets/warriors/deselect/11_1.PNG'
WD12_1= './lunarush/assets/warriors/deselect/12_1.PNG'
WD13_1 = './lunarush/assets/warriors/deselect/13_1.PNG'
WD14_1= './lunarush/assets/warriors/deselect/14_1.PNG'
WD15_1= './lunarush/assets/warriors/deselect/15_1.PNG'

START_BOSS_BTS = './lunarush/assets/start_boss_bt.PNG'
START_BOSS_2_BTS = './lunarush/assets/start_boss_2_bt.PNG'
START_FIGTH_BTS = './lunarush/assets/start_figth_bt.PNG'
RESULT_FIGTH_BTS = './lunarush/assets/result_figth_bt.PNG'
RESULT_FIGTH_2_BTS = './lunarush/assets/result_figth_2_bt.PNG'
COLLECT_REWERS_BTS = './lunarush/assets/collect_rewers_bt.PNG'
COLLECT_REWERS_2_BTS = './lunarush/assets/collect_rewers_2_bt.PNG'
RESULT_FIGTH_VICTORY_BTS = './lunarush/assets/result_figth_victory_bt.PNG'
RESULT_FIGTH_VICTORY_2_BTS = './lunarush/assets/result_figth_victory_2_bt.PNG'
ICONE_TAB_BTS = './lunarush/assets/icone_tab_bt.PNG'

def launch_luna_rush(): # 2m 57s
  image_click('Icon Refresf Luna', ICON_REFRESH_BTS, WAIT_TIME_LAUNCH) # 1m 54s
  image_click('Connect Wallet', CONNECT_WALLET_BTS, WAIT_START_BOSS) # 7s
  # image_one_click('Connect Wallet 2', CONNECT_WALLET_2_BTS, WAIT_START_BOSS) # 17s
  image_click('Sign Meta Mask', SIGN_META_MASK_BTS, WAIT_TIME_WALLET) # 27s
  image_click('Hunting Boss', HUNTING_BOSS_BTS, WAIT_HUNTING_BOSS) # 12s

def select_boss_level(): # 17s
  image_click('Select Level Boss', LEVEL_BOSS_SELECT_BTS, WAIT_HUNTING_BOSS) # 17s

def expand_tab_warriors(): # 17s
  image_click('Expand Warriors', EXPAND_WARRIORS_BTS, WAIT_HUNTING_BOSS) # 17s

def select_group_one(): # 1m
  image_one_click('Warrior 1 Select', WS1, WAIT_HUNTING_BOSS) # 10s
  image_one_click('Warrior 2 Select', WS2, WAIT_HUNTING_BOSS) # 10s
  image_one_click('Warrior 3 Select', WS3, WAIT_HUNTING_BOSS) # 10s
  image_one_click('Warrior 1 Select', WS1_1, WAIT_HUNTING_BOSS) # 10s
  image_one_click('Warrior 2 Select', WS2_1, WAIT_HUNTING_BOSS) # 10s
  image_one_click('Warrior 3 Select', WS3_1, WAIT_HUNTING_BOSS) # 10s

def select_group_two(): # 1m
  image_one_click('Warrior 4 Select', WS4, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 5 Select', WS5, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 6 Select', WS6, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 4 Select', WS4_1, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 5 Select', WS5_1, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 6 Select', WS6_1, WAIT_HUNTING_BOSS) # 12s

def select_group_three(): # 1m
  image_one_click('Warrior 7 Select', WS7, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 8 Select', WS8, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 9 Select', WS9, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 7 Select', WS7_1, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 8 Select', WS8_1, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 9 Select', WS9_1, WAIT_HUNTING_BOSS) # 12s

def select_group_for(): # 1m
  image_one_click('Warrior 10 Select', WS10, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 11 Select', WS11, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 12 Select', WS12, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 10 Select', WS10_1, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 11 Select', WS11_1, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 12 Select', WS12_1, WAIT_HUNTING_BOSS) # 12s

def select_group_five(): # 1m
  image_one_click('Warrior 13 Select', WS13, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 14 Select', WS14, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 15 Select', WS15, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 13 Select', WS13_1, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 14 Select', WS14_1, WAIT_HUNTING_BOSS) # 12s
  image_one_click('Warrior 15 Select', WS15_1, WAIT_HUNTING_BOSS) # 12s

def scroll_heros(mode): # 8s
  if mode:
    pyautogui.moveTo(1650,235)
    time.sleep(1)
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.moveTo(1650,150,1)
    time.sleep(1)
    pyautogui.mouseUp(button='left')

    pyautogui.moveTo(2165,235)
    time.sleep(1)
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.moveTo(2165,150,1)
    time.sleep(1)
    pyautogui.mouseUp(button='left')
  else:
    pyautogui.moveTo(1650,150)
    time.sleep(1)
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.moveTo(1650,235,1)
    time.sleep(1)
    pyautogui.mouseUp(button='left')

    pyautogui.moveTo(2165,150)
    time.sleep(1)
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.moveTo(2165,235,1)
    time.sleep(1)
    pyautogui.mouseUp(button='left')

def deselect_group_one(): # 1m
  image_click('Warrior Deselect', DELETE_ALL, WAIT_HUNTING_BOSS)
  # image_one_click('Warrior 1 Deselect', WD1, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 2 Deselect', WD2, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 3 Deselect', WD3, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 1 Deselect', WD1_1, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 2 Deselect', WD2_1, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 3 Deselect', WD3_1, WAIT_HUNTING_BOSS) # 12s

def deselect_group_two(): # 1m
  image_click('Warrior Deselect', DELETE_ALL, WAIT_HUNTING_BOSS)
  # image_one_click('Warrior 4 Deselect', WD4, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 5 Deselect', WD5, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 6 Deselect', WD6, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 4 Deselect', WD4_1, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 5 Deselect', WD5_1, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 6 Deselect', WD6_1, WAIT_HUNTING_BOSS) # 12s

def deselect_group_three(): # 1m
  image_click('Warrior Deselect', DELETE_ALL, WAIT_HUNTING_BOSS)
  # image_one_click('Warrior 7 Deselect', WD7, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 8 Deselect', WD8, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 9 Deselect', WD9, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 7 Deselect', WD7_1, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 8 Deselect', WD8_1, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 9 Deselect', WD9_1, WAIT_HUNTING_BOSS) # 12s

def deselect_group_for(): # 1m
  image_click('Warrior Deselect', DELETE_ALL, WAIT_HUNTING_BOSS)
  # image_one_click('Warrior 10 Deselect', WD10, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 11 Deselect', WD11, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 12 Deselect', WD12, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 10 Deselect', WD10_1, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 11 Deselect', WD11_1, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 12 Deselect', WD12_1, WAIT_HUNTING_BOSS) # 12s

def deselect_group_five(): # 1m
  image_click('Warrior Deselect', DELETE_ALL, WAIT_HUNTING_BOSS)
  # image_one_click('Warrior 13 Deselect', WD13, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 14 Deselect', WD14, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 15 Deselect', WD15, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 13 Deselect', WD13_1, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 14 Deselect', WD14_1, WAIT_HUNTING_BOSS) # 12s
  # image_one_click('Warrior 15 Deselect', WD15_1, WAIT_HUNTING_BOSS) # 12s

def figth_boss(): # 1m 54s
  image_one_click('Start Boss 1', START_BOSS_BTS) # 7s
  image_one_click('Start Boss 2', START_BOSS_2_BTS, WAIT_FIGTH_BOSS) # 55s
  image_one_click('Lose Figth 1', RESULT_FIGTH_BTS) # 7s
  image_one_click('Lose Figth 2', RESULT_FIGTH_2_BTS, WAIT_HUNTING_BOSS) # 10s
  image_one_click('Collect Rewers 1', COLLECT_REWERS_BTS) # 7s
  image_one_click('Collect Rewers 2', COLLECT_REWERS_2_BTS, WAIT_HUNTING_BOSS) # 10s
  image_one_click('Victory Figth 1', RESULT_FIGTH_VICTORY_BTS) # 7s
  image_one_click('Victory Figth 2', RESULT_FIGTH_VICTORY_2_BTS, WAIT_HUNTING_BOSS) # 10s

def close_luna_game(): # 7s
  image_click('Icon Refresf Luna', ICON_REFRESH_BTS) # 7s

def play_bot_luna():
  launch_luna_rush()
  select_boss_level()
  expand_tab_warriors()
  deselect_group_one()
  select_group_three()
  for figth in range(3):
    figth_boss()
    select_boss_level()
  expand_tab_warriors()
  deselect_group_three()
  select_group_two()
  for figth in range(3):
    figth_boss()
    select_boss_level()
  expand_tab_warriors()
  deselect_group_two()
  select_group_one()
  for figth in range(3):
    figth_boss()
    select_boss_level()
  close_luna_game()