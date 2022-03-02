import pyautogui
import sys
import time
from datetime import datetime

from fishcrypto.account import account

accountOne = account(
  name='FishCrypto - Conta 1',
  launchButton=[360,1000],
  loginMetaMaskButton=[430,955],
  signMetaMaskButton=[760,985],
  rod1tButton=[240,955],
  rod2tButton=[450,970],
  rod3tButton=[625,940],
  rodFriend1tButton=[772,872],
  selectFristRodButton=[710,655],
  pickRodButton=[600,1020],
  friendListButton=[750,651],
  rodFrientSelectButton=[545,650],
  newTabChromeButton=[274,554],
  closeTabChromeButton=[236,553],
)

accounts = [accountOne]

def launch_fish_crypto_single(name, launchButton, loginMetaMaskButton, signMetaMaskButton):
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

def launch_fish():
  for account in accounts:
    launch_fish_crypto_single(account.name, account.launchButton, account.loginMetaMaskButton, account.signMetaMaskButton)

def play_rod_fish(name, rodButton, selectFristRodButton, pickRodButton):
  pyautogui.moveTo(rodButton[0], rodButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Rod Button Press [OK]'%(name))
  time.sleep(20)
  pyautogui.moveTo(selectFristRodButton[0], selectFristRodButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Select First Button Press [OK]'%(name))
  time.sleep(10)
  pyautogui.moveTo(pickRodButton[0], pickRodButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Pick Rod Button Press [OK]'%(name))
  time.sleep(30)

def play_rod_one_fish():
  for account in accounts:
    play_rod_fish(account.name, account.rod1tButton, account.selectFristRodButton, account.pickRodButton)

def play_rod_two_fish():
  for account in accounts:
    play_rod_fish(account.name, account.rod2tButton, account.selectFristRodButton, account.pickRodButton)

def play_rod_three_fish():
  for account in accounts:
    play_rod_fish(account.name, account.rod3tButton, account.selectFristRodButton, account.pickRodButton)

def play_friend_rod_fish_single(name, rodFriendButton, friendListButton, rodFrientSelectButton, pickRodButton):
  pyautogui.moveTo(rodFriendButton[0], rodFriendButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Rod Button Press [OK]'%(name))
  time.sleep(20)
  pyautogui.moveTo(friendListButton[0], friendListButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Select Friend Button Press [OK]'%(name))
  time.sleep(10)
  pyautogui.moveTo(rodFrientSelectButton[0], rodFrientSelectButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Select Rod Button Press [OK]'%(name))
  time.sleep(15)
  pyautogui.moveTo(pickRodButton[0], pickRodButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Pick Rod Button Press [OK]'%(name))
  time.sleep(15)

def play_friend_rod_fish():
  for account in accounts:
    play_friend_rod_fish_single(account.name, account.rodFriend1tButton, account.friendListButton, account.rodFrientSelectButton, account.pickRodButton)

def close_game_single(name, newTabChromeButton, closeTabChromeButton):
  pyautogui.moveTo(newTabChromeButton[0], newTabChromeButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] New Tab Chrome Button Press [OK]'%(name))
  time.sleep(5)
  pyautogui.moveTo(closeTabChromeButton[0], closeTabChromeButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Close Tab Chrome Button Press [OK]'%(name))
  time.sleep(5)

def close_fish_game():
  for account in accounts:
    close_game_single(account.name, account.newTabChromeButton, account.closeTabChromeButton)

def play_bot_fish(): #  9 minutos e 10 segundos
  launch_fish() # 2 minutos
  play_rod_one_fish() # 1 minuto
  play_rod_two_fish() # 2 minuto
  play_rod_three_fish() # 3 minuto
  play_friend_rod_fish() # 1 minuto
  close_fish_game() # 10 segundos