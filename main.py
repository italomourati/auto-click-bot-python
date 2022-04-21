from bombcrypto.main import play_heros, refresh_heros, open_and_close_trunk, play_bot_bomb, connect_bomb
from lunarush.main import launch_luna_rush, select_boss_level, select_group_one, select_group_two, select_group_three, select_group_for, select_group_five, deselect_group_one, deselect_group_two, deselect_group_three, deselect_group_for, deselect_group_five, figth_boss, close_luna_game, play_bot_luna, expand_tab_warriors, scroll_heros
import os
from pydoc import importfile

time_print = importfile('./modules/timeprint.py')

menu_options = {
  1: 'Executar bot BombCrypto',
  2: 'Executar bot LunaRush',
  3: 'Executar TODOS',
  0: 'Sair'
}

def print_menu():
  for key in menu_options:
    print(key, '-', menu_options[key])

# LUNA RUSH
def play_luna(): # 39m 33s
  launch_luna_rush() # 2m 57s
  select_boss_level() # 17s
  expand_tab_warriors() # 17s
  deselect_group_one() # 1m to 14s
  scroll_heros(True) # 8s
  select_group_five() # 1m
  for figth in range(3): # 6m 33s
    figth_boss() 
    select_boss_level()
  expand_tab_warriors() # 17s
  deselect_group_five() # 1m
  select_group_for() # 1m
  for figth in range(3): # 6m 33s
    figth_boss() 
    select_boss_level()
  expand_tab_warriors() # 17s
  deselect_group_for() # 1m
  select_group_three() # 1m
  for figth in range(3): # 6m 33s
    figth_boss() 
    select_boss_level()
  expand_tab_warriors() # 17s
  deselect_group_three() # 1m
  select_group_two() # 1m
  for figth in range(3): # 6m 33s
    figth_boss() 
    select_boss_level()
  expand_tab_warriors() # 17s
  deselect_group_two() # 1m
  select_group_one() # 1m
  for figth in range(3): # 6m 33s
    figth_boss() 
    select_boss_level()
  close_luna_game() # 13s

# NOT AFK BOMBCRYPTO 
def not_afk_bomb(loop):
  for item in range(loop): # 7m ou 5m 35s
    refresh_heros() # 22s
    time_print(120) # 2m
    open_and_close_trunk() # 22s
    time_print(120) # 2m
    connect_bomb() # 1m 45s ou 20s
    time_print(31) # 31s

def stage_one(): # 1h 30m 2s
  play_luna() # 39m 33s
  connect_bomb() # 1m 45s
  play_heros() # 1m 5s
  not_afk_bomb(4) # 28m ou 22m 20s
  play_heros() # 1m 5s
  not_afk_bomb(2) # 14m ou 11m 10s
  refresh_heros() # 22s
  time_print(120) # 2m
  open_and_close_trunk() # 22s
  time_print(120) # 2m
  refresh_heros() # 22s
  time_print(120) # 2m
  open_and_close_trunk() # 22s
  time_print(120) # 2m
  refresh_heros() # 22s
  time_print(120) # 2m
  open_and_close_trunk() # 22s
  time_print(120) # 2m

def stage_two(): # 1h 30m
  connect_bomb() # 1m 45s ou 20s
  play_heros() # 1m 5s
  not_afk_bomb(4) # 28m ou 22m 20s
  play_heros() # 1m 5s
  not_afk_bomb(4) # 28m ou 22m 20s
  play_heros() # 1m 5s
  not_afk_bomb(4) # 28m ou 22m 20s
  play_heros() # 1m 5s
  not_afk_bomb(3) # 21m ou 16m 45s
  play_heros() # 1m 5s
  time_print(30) # 30s

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
        play_bot_bomb() # 22
    
    if select == 2:
      while True:
        play_bot_luna() # 

    if select == 3:
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

main_menu()