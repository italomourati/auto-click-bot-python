from bombcrypto.main import play_heros, refresh_heros, open_and_close_trunk, play_bot_bomb, connect_bomb
from lunarush.main import launch_luna_rush, select_boss_level, select_group_one, select_group_two, select_group_three, deselect_group_one, deselect_group_two, deselect_group_three, figth_boss, close_luna_game, play_bot_luna, expand_tab_warriors
from spacecrypto.main import launch_space_crypto, close_space_game, play_ship_space, play_bot_space
from fishcrypto.main import play_bot_fish, launch_fish_crypto, pick_rod_player, pick_rod_friend, close_fish_game
import os
from pydoc import importfile

time_print = importfile('./modules/timeprint.py')

menu_options = {
  1: 'Executar bot BombCrypto',
  2: 'Executar bot LunaRush',
  3: 'Executar bot SpaceCrypto',
  4: 'Executar bot FishCrypto',
  5: 'Executar TODOS',
  0: 'Sair'
}

def print_menu():
  for key in menu_options:
    print(key, '-', menu_options[key])

# LUNA RUSH
def play_luna(): # 29m 18s
  launch_luna_rush() # 2m 7s
  refresh_heros() # 22s
  select_boss_level() # 12s
  expand_tab_warriors() # 12s
  deselect_group_one() # 36s
  select_group_three() # 36s
  for figth in range(3): # 6m 18s
    figth_boss() 
    select_boss_level()
    refresh_heros() # 22s
  expand_tab_warriors() # 12s
  deselect_group_three() # 36s
  select_group_two() # 36s
  for figth in range(3): # 6m 18s
    figth_boss() 
    select_boss_level()
    refresh_heros() # 22s 
  expand_tab_warriors() # 12s
  deselect_group_two() # 36s
  select_group_one() # 36s
  for figth in range(3): # 6m 18s
    figth_boss() 
    select_boss_level()
    refresh_heros() # 22s
  close_luna_game() # 13s

# SPACECRYPTO 
def play_space_crypto(): # 3m 24s
  launch_space_crypto() # 2m 8s
  play_ship_space() # 1m 16s

# FISH CRYPTO 
def play_fish_crypto(): # 4m 45s 
  launch_fish_crypto() # 1m 31s
  pick_rod_player() # 2m 3s
  pick_rod_friend() # 58s
  close_fish_game() # 13s

# NOT AFK BOMBCRYPTO 
def not_afk_bomb(): # 28m
  for item in range(4): # 7m
    refresh_heros() # 22s
    time_print(120) # 2m
    open_and_close_trunk() # 22s
    time_print(120) # 2m
    connect_bomb() # 1m 45s
    time_print(31) # 31s

def stage_one(): # 1h 30m
  refresh_heros() # 22s
  play_fish_crypto() # 4m 45s
  refresh_heros() # 22s
  play_luna() # 29m 18s
  play_space_crypto() # 3m 24s
  play_heros() # 1m 5s
  not_afk_bomb() #28m
  close_space_game() # 13s
  play_heros() # 1m 5s
  refresh_heros() # 22s
  time_print(120) # 2m
  open_and_close_trunk() # 22s
  time_print(120) # 2m
  connect_bomb() # 1m 45s
  time_print(31) # 31s
  refresh_heros() # 22s
  time_print(120) # 2m
  open_and_close_trunk() # 22s
  time_print(120) # 2m
  connect_bomb() # 1m 45s
  time_print(31) # 31s
  refresh_heros() # 22s
  time_print(120) # 2m
  open_and_close_trunk() # 22s
  time_print(120) # 2m
  connect_bomb() # 1m 45s
  time_print(31) # 31s
  refresh_heros() # 22s
  time_print(46) # 46s

def stage_two(): # 1h 30m
  play_heros() # 1m 5s
  not_afk_bomb() # 28m
  play_space_crypto() # 3m 24s
  play_heros() # 1m 5s
  not_afk_bomb() #28m
  close_space_game() # 13s
  play_heros() # 1m 5s
  not_afk_bomb() #28m
  play_heros() # 1m 5s

def stage_three(): # 1h 30m
  refresh_heros() # 22s
  time_print(120) # 2m
  open_and_close_trunk() # 22s
  time_print(120) # 2m
  refresh_heros() # 22s
  time_print(1) # 1s
  refresh_heros() # 22s
  play_luna() # 29m 18s
  play_space_crypto() # 3m 24s
  play_heros() # 1m 5s
  not_afk_bomb() #28m
  close_space_game() # 13s
  play_heros() # 1m 5s
  refresh_heros() # 22s
  time_print(120) # 2m
  open_and_close_trunk() # 22s
  time_print(120) # 2m
  connect_bomb() # 1m 45s
  time_print(31) # 31s
  refresh_heros() # 22s
  time_print(120) # 2m
  open_and_close_trunk() # 22s
  time_print(120) # 2m
  connect_bomb() # 1m 45s
  time_print(31) # 31s
  refresh_heros() # 22s
  time_print(120) # 2m
  open_and_close_trunk() # 22s
  time_print(120) # 2m
  connect_bomb() # 1m 45s
  time_print(31) # 31s
  refresh_heros() # 22s
  time_print(46) # 46s

def main_menu():
  while True:
    os.system('cls' if os.name == 'nt' else 'clear') # limpar console
    print('########## BEM VINDO AO BOT CRYPTO BY: ITALO MOURA ##########\n')
    print_menu()
    select = int(input('\nDigite o numero para executar: '))
    
    if select == 0:
      exit()

    if select == 1:
      while True:
        play_bot_bomb() # 
    
    if select == 2:
      while True:
        play_bot_luna() # 

    if select == 3:
      while True:
        play_bot_space() #

    if select == 4:
      while True:
        play_bot_fish() #

    if select == 5:
      while True:
        os.system('cls' if os.name == 'nt' else 'clear') # limpar console
        print('############### FASE 1 ###############')
        stage_one() # 1h 30m
        os.system('cls' if os.name == 'nt' else 'clear') # limpar console
        print('############### FASE 2 ###############')
        stage_two() # 1h 30m
        os.system('cls' if os.name == 'nt' else 'clear') # limpar console
        print('############### FASE 3 ###############')
        stage_two() # 1h 30m
        os.system('cls' if os.name == 'nt' else 'clear') # limpar console
        print('############### FASE 4 ###############')
        stage_three() # 1h 30m
        os.system('cls' if os.name == 'nt' else 'clear') # limpar console
        print('############### FASE 5 ###############')
        stage_two() # 1h 30m
        os.system('cls' if os.name == 'nt' else 'clear') # limpar console
        print('############### FASE 6 ###############')
        stage_two() # 1h 30m

main_menu()