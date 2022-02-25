import pyautogui
import sys
import time
from datetime import datetime

from bombcrypto.account import account

accountOne = account(
  name='BombCrypto - Conta 1',
  backButton=[140,135], 
  mapButton=[430,320],
  trunkButton=[675,140],
  trunkCloseButton=[605,190],
  heroButton=[700,465],
  allPlayHeroButton=[373,220],
  heroCloseButton=[465,190],
)

accountTwo = account(
  name='BombCrypto - Conta 2',
  backButton=[990,135], 
  mapButton=[1280,320],
  trunkButton=[1525,140],
  trunkCloseButton=[1460,190],
  heroButton=[1555,465],
  allPlayHeroButton=[1225,220],
  heroCloseButton=[1320,190],
)

accountThree = account(
  name='BombCrypto - Conta 3',
  backButton=[((accountTwo.backButton[0] - accountOne.backButton[0]) + accountTwo.backButton[0]),135], 
  mapButton=[((accountTwo.mapButton[0] - accountOne.mapButton[0]) + accountTwo.mapButton[0]),320],
  trunkButton=[((accountTwo.trunkButton[0] - accountOne.trunkButton[0]) + accountTwo.trunkButton[0]),140],
  trunkCloseButton=[((accountTwo.trunkCloseButton[0] - accountOne.trunkCloseButton[0]) + accountTwo.trunkCloseButton[0]),190],
  heroButton=[((accountTwo.heroButton[0] - accountOne.heroButton[0]) + accountTwo.heroButton[0]),465],
  allPlayHeroButton=[((accountTwo.allPlayHeroButton[0] - accountOne.allPlayHeroButton[0]) + accountTwo.allPlayHeroButton[0]),220],
  heroCloseButton=[((accountTwo.heroCloseButton[0] - accountOne.heroCloseButton[0]) + accountTwo.heroCloseButton[0]),190],
)

accounts = [accountOne, accountTwo, accountThree]

def refresh_hero_single(name, backButton, mapButton):
  pyautogui.moveTo(backButton[0], backButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Back Button Press [OK]'%(name))
  time.sleep(2)
  pyautogui.moveTo(mapButton[0], mapButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Map Button Press [OK]'%(name))
  time.sleep(2)

def refresh_hero():
  for account in accounts:
    refresh_hero_single(account.name, account.backButton, account.mapButton)

def open_trunk_single(name, backButton, mapButton):
  pyautogui.moveTo(backButton[0], backButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Trunk Button Press [OK]'%(name))
  time.sleep(2)
  pyautogui.moveTo(mapButton[0], mapButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Trunk Close Button Press [OK]'%(name))
  time.sleep(2)

def open_trunk():
  for account in accounts:
    open_trunk_single(account.name, account.trunkButton, account.trunkCloseButton)

def play_hero_job_single(name, backButton, heroButton, allPlayHeroButton, heroCloseButton, mapButton):
  pyautogui.moveTo(backButton[0], backButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Back Button Press [OK]'%(name))
  time.sleep(2)
  pyautogui.moveTo(heroButton[0], heroButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Hero Button Press [OK]'%(name))
  time.sleep(10)
  pyautogui.moveTo(allPlayHeroButton[0], allPlayHeroButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] All Hero Button Press [OK]'%(name))
  time.sleep(6)
  pyautogui.moveTo(heroCloseButton[0], heroCloseButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Hero Close Button Press [OK]'%(name))
  time.sleep(2)
  pyautogui.moveTo(mapButton[0], mapButton[1])
  pyautogui.click()
  print(datetime.now().strftime('%d/%m %H:%M:%S'),'[%s] Map Button Press [OK]'%(name))
  time.sleep(2)

def play_hero_job():
  for account in accounts:
    play_hero_job_single(account.name, account.backButton, account.heroButton, account.allPlayHeroButton, account.heroCloseButton, account.mapButton)

def play_bot_bomb(): # 47 minutos e 6 segundos 
  play_hero_job() # 1 minuto e 6 segundos
  time.sleep(120) # 2 minutos

  for item in range(10):
    refresh_hero() # 12 segundos
    time.sleep(120) # 2 minutos
    open_trunk() # 12 segundos
    time.sleep(120) # 2 minutos