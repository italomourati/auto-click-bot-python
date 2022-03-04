from pydoc import importfile
from re import T
import pyautogui
import time
from datetime import datetime
from colorama import init, Fore, Style

init(convert=True)

image_click = importfile('./modules/imageclick.py')

WAIT_TIME_LAUNCH = 50
WAIT_TIME_WALLET = 20
WAIT_HUNTING_BOSS = 5
WAIT_START_BOSS = 10
WAIT_FIGTH_BOSS = 50

ICON_LUNA_BTS = './lunarush/assets/icon_luna_bt.PNG'
CONNECT_WALLET_BTS = './lunarush/assets/connect_meta_mask_bt.PNG'
SIGN_META_MASK_BTS = './lunarush/assets/sign_meta_mask_bt.PNG'
HUNTING_BOSS_BTS = './lunarush/assets/hunting_boss_bt.PNG'
LEVEL_BOSS_SELECT_BTS = './lunarush/assets/level_boss_bt.PNG'
EXPAND_WARRIORS_BTS = './lunarush/assets/expand_warriors_bt.PNG'
WARRIOR_1_BTS = './lunarush/assets/warrior_1_bt.PNG'
WARRIOR_2_BTS = './lunarush/assets/warrior_2_bt.PNG'
WARRIOR_3_BTS = './lunarush/assets/warrior_3_bt.PNG'
WARRIOR_4_BTS = './lunarush/assets/warrior_4_bt.PNG'
WARRIOR_5_BTS = './lunarush/assets/warrior_5_bt.PNG'
WARRIOR_6_BTS = './lunarush/assets/warrior_6_bt.PNG'
WARRIOR_7_BTS = './lunarush/assets/warrior_7_bt.PNG'
WARRIOR_8_BTS = './lunarush/assets/warrior_8_bt.PNG'
WARRIOR_9_BTS = './lunarush/assets/warrior_9_bt.PNG'
WARRIOR_1_SELECT_BTS = './lunarush/assets/warrior_1_select_bt.PNG'
WARRIOR_2_SELECT_BTS = './lunarush/assets/warrior_2_select_bt.PNG'
WARRIOR_3_SELECT_BTS = './lunarush/assets/warrior_3_select_bt.PNG'
WARRIOR_4_SELECT_BTS = './lunarush/assets/warrior_4_select_bt.PNG'
WARRIOR_5_SELECT_BTS = './lunarush/assets/warrior_5_select_bt.PNG'
WARRIOR_6_SELECT_BTS = './lunarush/assets/warrior_6_select_bt.PNG'
WARRIOR_7_SELECT_BTS = './lunarush/assets/warrior_7_select_bt.PNG'
WARRIOR_8_SELECT_BTS = './lunarush/assets/warrior_8_select_bt.PNG'
WARRIOR_9_SELECT_BTS = './lunarush/assets/warrior_9_select_bt.PNG'
START_BOSS_BTS = './lunarush/assets/start_boss_bt.PNG'
START_FIGTH_BTS = './lunarush/assets/start_figth_bt.PNG'
RESULT_FIGTH_BTS = './lunarush/assets/result_figth_bt.PNG'
COLLECT_REWERS_BTS = './lunarush/assets/collect_rewers_bt.PNG'
RESULT_FIGTH_VICTORY_BTS = './lunarush/assets/result_figth_victory_bt.PNG'
ICONE_TAB_BTS = './lunarush/assets/icone_tab_bt.PNG'

def launch_luna_rush(): # 2m 7s
  image_click('Icon Luna', ICON_LUNA_BTS, WAIT_TIME_LAUNCH) #1m 1s
  image_click('Connect Wallet', CONNECT_WALLET_BTS, WAIT_TIME_WALLET) # 27s
  image_click('Sign Meta Mask', SIGN_META_MASK_BTS, WAIT_TIME_WALLET) # 27s
  image_click('Hunting Boss', HUNTING_BOSS_BTS, WAIT_HUNTING_BOSS) # 12s

def select_boss_level(): # 12s
  image_click('Select Level Boss', LEVEL_BOSS_SELECT_BTS, WAIT_HUNTING_BOSS) # 12s

def select_group_one(): # 36s
  image_click('Warrior 1 Select', WARRIOR_1_BTS, WAIT_HUNTING_BOSS) # 12s
  image_click('Warrior 2 Select', WARRIOR_2_BTS, WAIT_HUNTING_BOSS) # 12s
  image_click('Warrior 3 Select', WARRIOR_3_BTS, WAIT_HUNTING_BOSS) # 12s

def select_group_two(): # 36s
  image_click('Warrior 4 Select', WARRIOR_4_BTS, WAIT_HUNTING_BOSS) # 12s
  image_click('Warrior 5 Select', WARRIOR_5_BTS, WAIT_HUNTING_BOSS) # 12s
  image_click('Warrior 6 Select', WARRIOR_6_BTS, WAIT_HUNTING_BOSS) # 12s

def select_group_three(): # 36s
  image_click('Warrior 7 Select', WARRIOR_7_BTS, WAIT_HUNTING_BOSS) # 12s
  image_click('Warrior 8 Select', WARRIOR_8_BTS, WAIT_HUNTING_BOSS) # 12s
  image_click('Warrior 9 Select', WARRIOR_9_BTS, WAIT_HUNTING_BOSS) # 12s

def deselect_group_one(): # 36s
  image_click('Warrior 1 Deselect', WARRIOR_1_SELECT_BTS, WAIT_HUNTING_BOSS) # 12s
  image_click('Warrior 2 Deselect', WARRIOR_2_SELECT_BTS, WAIT_HUNTING_BOSS) # 12s
  image_click('Warrior 3 Deselect', WARRIOR_3_SELECT_BTS, WAIT_HUNTING_BOSS) # 12s

def deselect_group_two(): # 36s
  image_click('Warrior 4 Deselect', WARRIOR_4_SELECT_BTS, WAIT_HUNTING_BOSS) # 12s
  image_click('Warrior 5 Deselect', WARRIOR_5_SELECT_BTS, WAIT_HUNTING_BOSS) # 12s
  image_click('Warrior 6 Deselect', WARRIOR_6_SELECT_BTS, WAIT_HUNTING_BOSS) # 12s

def deselect_group_three(): # 36s
  image_click('Warrior 7 Deselect', WARRIOR_7_SELECT_BTS, WAIT_HUNTING_BOSS) # 12s
  image_click('Warrior 8 Deselect', WARRIOR_8_SELECT_BTS, WAIT_HUNTING_BOSS) # 12s
  image_click('Warrior 9 Deselect', WARRIOR_9_SELECT_BTS, WAIT_HUNTING_BOSS) # 12s

def figth_boss(): # 1m 54s
  image_click('Start Boss', START_BOSS_BTS, WAIT_START_BOSS) # 17s
  image_click('Start Figth', START_FIGTH_BTS, WAIT_FIGTH_BOSS) # 1m 1s
  image_click('Lose Figth', RESULT_FIGTH_BTS, WAIT_HUNTING_BOSS) # 12s
  image_click('Collect Rewers', COLLECT_REWERS_BTS, WAIT_HUNTING_BOSS) # 12s
  image_click('Victory Figth', RESULT_FIGTH_VICTORY_BTS, WAIT_HUNTING_BOSS) # 12s

def close_luna_game(): # 13s
  image_click('Icon Tab', ICONE_TAB_BTS) # 7s
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

def expand_tab_warriors(): # 12s
  image_click('Expand Warriors', EXPAND_WARRIORS_BTS, WAIT_HUNTING_BOSS) # 12s

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