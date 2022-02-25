import pyautogui
import sys
import time
from datetime import datetime

from lunarush.account import account

accountOne = account(
  name='LunaRush - Conta 1',
  launchButton=[1200,1000],
  loginMetaMaskButton=[1415,890],
  signMetaMaskButton=[1605,980],
  bossMenuButton=[1085,800],
  boss1Button=[1240,760],
  boss2Button=[1295,905],
  boss3Button=[1412,760],
  hero1SlotButton=[1000,745],
  hero2SlotButton=[1065,745],
  hero3SlotButton=[1000,835],
  hero4SlotButton=[1065,835],
  hero5SlotButton=[1000,920],
  hero6SlotButton=[1065,920],
  hero7SlotButton=[1000,835],
  hero8SlotButton=[1065,835],
  hero9SlotButton=[1000,920],
  hunterBossButton=[1510,955],
  startFightBossClick=[1260,830],
  collectRewardButton=[1275,945],
  newTabChromeButton=[1125,553],
  closeTabChromeButton=[1088,551],
)

accounts = [accountOne]

def launch_luna_rush_single(name, launchButton, loginMetaMaskButton, signMetaMaskButton, bossMenuButton):
  pyautogui.moveTo(launchButton[0], launchButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Launch Button Press [OK]'%(name))
  time.sleep(60)
  pyautogui.moveTo(loginMetaMaskButton[0], loginMetaMaskButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Login MetaMask Button Press [OK]'%(name))
  time.sleep(15)
  pyautogui.moveTo(signMetaMaskButton[0], signMetaMaskButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Sign MetaMask Button Press [OK]'%(name))
  time.sleep(45)
  pyautogui.moveTo(bossMenuButton[0], bossMenuButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Boss Menu Button Press [OK]'%(name))
  time.sleep(5)

def launch_luna():
  for account in accounts:
    launch_luna_rush_single(account.name, account.launchButton, account.loginMetaMaskButton, account.signMetaMaskButton, account.bossMenuButton)

def select_boss_level_one_single(name, boss1Button, boss2Button, boss3Button):
  pyautogui.moveTo(boss1Button[0], boss1Button[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Boss Level 1 Button Press [OK]'%(name))
  time.sleep(5)
  pyautogui.moveTo(boss2Button[0], boss2Button[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Boss Level 2 Button Press [OK]'%(name))
  time.sleep(5)
  pyautogui.moveTo(boss3Button[0], boss3Button[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Boss Level 3 Button Press [OK]'%(name))
  time.sleep(5)

def select_boss_level_one():
  for account in accounts:
    select_boss_level_one_single(account.name, account.boss1Button, account.boss2Button, account.boss3Button)

def select_heros_single(name, hero1, hero2, hero3):
  pyautogui.moveTo(hero1[0], hero1[1], 1)
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Hero 1 ou 4 Select Button Press [OK]'%(name))
  time.sleep(10)
  pyautogui.moveTo(hero2[0], hero2[1], 1)
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Hero 2 ou 5 Select Button Press [OK]'%(name))
  time.sleep(10)
  pyautogui.moveTo(hero3[0], hero3[1], 1)
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Hero 3 ou 6 Select Button Press [OK]'%(name))
  time.sleep(10)

def select_heros_one_two_three():
  for account in accounts:
    select_heros_single(account.name, account.hero1SlotButton, account.hero2SlotButton, account.hero3SlotButton)

def select_heros_for_five_six():
  for account in accounts:
    select_heros_single(account.name, account.hero4SlotButton, account.hero5SlotButton, account.hero6SlotButton)

def select_heros_seven_eight_nine():
  for account in accounts:
    select_heros_single(account.name, account.hero7SlotButton, account.hero8SlotButton, account.hero9SlotButton)

def figth_boss_single(name, hunterBossButton, startFightBossClick, collectRewardButton):
  pyautogui.moveTo(hunterBossButton[0], hunterBossButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Hunter Boss Button Press [OK]'%(name))
  time.sleep(10)
  pyautogui.moveTo(startFightBossClick[0], startFightBossClick[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Start Fight Button Press [OK]'%(name))
  time.sleep(60)
  pyautogui.moveTo(collectRewardButton[0], collectRewardButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Collect Reward Button Press [OK]'%(name))
  time.sleep(10)
  pyautogui.moveTo(collectRewardButton[0], collectRewardButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Collect Reward Button Press [OK]'%(name))
  time.sleep(10)

def figth_boss():
  for account in accounts:
    figth_boss_single(account.name, account.hunterBossButton, account.startFightBossClick, account.collectRewardButton)

def close_game_single(name, newTabChromeButton, closeTabChromeButton):
  pyautogui.moveTo(newTabChromeButton[0], newTabChromeButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] New Tab Chrome Button Press [OK]'%(name))
  time.sleep(10)
  pyautogui.moveTo(closeTabChromeButton[0], closeTabChromeButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Close Tab Chrome Button Press [OK]'%(name))
  time.sleep(10)

def close_game():
  for account in accounts:
    close_game_single(account.name, account.newTabChromeButton, account.closeTabChromeButton)

def scroll_mouse_heros_single(name, mode):
  if mode:
    pyautogui.moveTo(1030,875)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(1030,690,1)
    pyautogui.mouseUp(button='left')
    print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Scroll Last Heros [OK]'%(name))
    time.sleep(10)
  else :
    pyautogui.moveTo(1030,690)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(1030,875,1)
    pyautogui.mouseUp(button='left')
    print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Scroll First Heros [OK]'%(name))
    time.sleep(10)

def scroll_mouse_heros(mode):
  for account in accounts:
    scroll_mouse_heros_single(account.name, mode)


def play_bot_luna(): # 4 horas 49 minutos e 56 segundos
  launch_luna() # 2 minutos
  select_boss_level_one() # 20 segundos
  select_heros_one_two_three() # 30 segundos
  scroll_mouse_heros(True) # 12 seggundos
  select_heros_seven_eight_nine() # 30 segundos
  figth_boss() # 1 minuto e 30 segundos
  figth_boss() # 1 minuto e 30 segundos
  figth_boss() # 1 minuto e 30 segundos
  select_heros_seven_eight_nine() # 30 segundos
  scroll_mouse_heros(False) # 12 seggundos
  select_heros_for_five_six() # 30 segundos
  figth_boss() # 1 minuto e 30 segundos
  figth_boss() # 1 minuto e 30 segundos
  figth_boss() # 1 minuto e 30 segundos
  select_heros_for_five_six() # 30 segundos
  select_heros_one_two_three() # 30 segundos
  figth_boss() # 1 minuto e 30 segundos
  figth_boss() # 1 minuto e 30 segundos
  figth_boss() # 1 minuto e 30 segundos
  close_game() # 20 segundos
  time.sleep(16200); # 4 horas e 30 minutos