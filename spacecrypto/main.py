import pyautogui
import sys
import time
from datetime import datetime

from spacecrypto.account import account

accountOne = account(
  name='SpaceCrypto - Conta 1',
  launchButton=[2120,1000],
  loginMetaMaskButton=[2130,910],
  tabMetaMask=[2390,540],
  tabMetaMaskDrag=[2381,448],
  signMetaMaskButton=[2450,990],
  playSpaceButton=[2134,910],
  navFightButton=[2225,740],
  fightBossButton=[2365,945],
  loseButton=[2130,890],
  newTabChromeButton=[1977,553],
  closeTabChromeButton=[1940,550],
)

accounts = [accountOne]

def launch_space_crypto_single(name, launchButton, loginMetaMaskButton, tabMetaMask, tabMetaMaskDrag, signMetaMaskButton):
  pyautogui.moveTo(launchButton[0], launchButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Launch Button Press [OK]'%(name))
  time.sleep(60)
  pyautogui.moveTo(loginMetaMaskButton[0], loginMetaMaskButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Login MetaMask Button Press [OK]'%(name))
  time.sleep(15)
  pyautogui.moveTo(tabMetaMask[0], tabMetaMask[1])
  pyautogui.mouseDown(button='left')
  pyautogui.moveTo(tabMetaMaskDrag[0],tabMetaMaskDrag[1],1)
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Tab MetaMask Button Press [OK]'%(name))
  time.sleep(5)
  pyautogui.mouseUp(button='left')
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Tab Drag MetaMask Button Press [OK]'%(name))
  time.sleep(5)
  pyautogui.moveTo(signMetaMaskButton[0], signMetaMaskButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Sign MetaMask Button Press [OK]'%(name))
  time.sleep(45)

def launch_space():
  for account in accounts:
    launch_space_crypto_single(account.name, account.launchButton, account.loginMetaMaskButton, account.tabMetaMask, account.tabMetaMaskDrag, account.signMetaMaskButton)

def fight_boss_single(name, playSpaceButton, navFightButton, fightBossButton, loseButton):
  pyautogui.moveTo(playSpaceButton[0], playSpaceButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Play Space Button Press [OK]'%(name))
  time.sleep(20)

  for nav in range(15):
    pyautogui.moveTo(navFightButton[0], navFightButton[1])
    pyautogui.click()
    print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Nav Fight Button Press [OK]'%(name))
    time.sleep(5)

  pyautogui.moveTo(fightBossButton[0], fightBossButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Fight Boss Button Press [OK]'%(name))
  time.sleep(10)
  pyautogui.moveTo(loseButton[0], loseButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Lose Button Press [OK]'%(name))
  time.sleep(15)

def fight_boss():
  for account in accounts:
    fight_boss_single(account.name, account.playSpaceButton, account.navFightButton, account.fightBossButton, account.loseButton)

def close_game_single(name, newTabChromeButton, closeTabChromeButton):
  pyautogui.moveTo(newTabChromeButton[0], newTabChromeButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] New Tab Chrome Button Press [OK]'%(name))
  time.sleep(5)
  pyautogui.moveTo(closeTabChromeButton[0], closeTabChromeButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Close Tab Chrome Button Press [OK]'%(name))
  time.sleep(5)

def close_space_game():
  for account in accounts:
    close_game_single(account.name, account.newTabChromeButton, account.closeTabChromeButton)

def play_bot_space(): # 24 minutos e 20 segundos
  launch_space() # 2 minutos e 10 segundos
  fight_boss() # 2 minutos
  time.sleep(1200) # 20 minutos
  close_space_game() # 10 segundos