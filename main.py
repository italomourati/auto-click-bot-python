from bombcrypto.main import play_hero_job, refresh_hero, open_trunk, play_bot_bomb
from lunarush.main import launch_luna, select_boss_level_one, select_heros_one_two_three, select_heros_for_five_six, figth_boss, close_game, play_bot_luna, scroll_mouse_heros, select_heros_seven_eight_nine
from spacecrypto.main import launch_space, fight_boss, close_space_game, play_bot_space
import os
import time

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

# LUNA 23 MINUTOS  34 segundos
def play_luna(): 
  launch_luna() # 2 minutos
  select_boss_level_one() # 20 segundos
  select_heros_one_two_three() # 30 segundos
  scroll_mouse_heros(True) # 12 seggundos
  select_heros_seven_eight_nine() # 30 segundos
  refresh_hero() # 12 segundos
  figth_boss() # 1 minuto e 30 segundos
  select_boss_level_one() # 20 segundos
  figth_boss() # 1 minuto e 30 segundos
  select_boss_level_one() # 20 segundos
  figth_boss() # 1 minuto e 30 segundos
  refresh_hero() # 12 segundos
  select_boss_level_one() # 20 segundos
  scroll_mouse_heros(True) # 12 seggundos
  select_heros_seven_eight_nine() # 30 segundos
  scroll_mouse_heros(False) # 12 seggundos
  select_heros_for_five_six() # 30 segundos
  refresh_hero() # 12 segundos
  figth_boss() # 1 minuto e 30 segundos
  select_boss_level_one() # 20 segundos
  figth_boss() # 1 minuto e 30 segundos
  select_boss_level_one() # 20 segundos
  figth_boss() # 1 minuto e 30 segundos
  refresh_hero() # 12 segundos
  select_boss_level_one() # 20 segundos
  select_heros_for_five_six() # 30 segundos
  select_heros_one_two_three() # 30 segundos
  refresh_hero() # 12 segundos
  figth_boss() # 1 minuto e 30 segundos
  select_boss_level_one() # 20 segundos
  figth_boss() # 1 minuto e 30 segundos
  select_boss_level_one() # 20 segundos
  figth_boss() # 1 minuto e 30 segundos
  select_boss_level_one() # 20 segundos
  close_game() # 20 segundos
  refresh_hero() # 12 segundos

# SPACECRYPTO 4 MINUTOS E 10 SEGUNDOS
def play_space_crypto():
  launch_space() # 2 minutos e 10 segundos
  fight_boss() # 2 minutos

# NOT AFK BOMBCRYPTO 22 MINUTOS
def not_afk_bomb():
  for item in range(5): 
    refresh_hero() # 12 segundos
    time.sleep(120) # 2 minutos
    open_trunk() # 12 segundos
    time.sleep(120) # 2 minutos

# 1 HORA 30 MINUTO
def stage_one():
  play_luna() # 23 MINUTOS e 34 segundos
  play_space_crypto() # 4 MINUTOS e 10 SEGUNDOS
  play_hero_job() # 1 MINUTOS e 6 SEGUNDOS
  not_afk_bomb() # 22 MINUTOS
  close_space_game(); # 10 SEGUNDOS
  not_afk_bomb() # 22 MINUTOS
  play_hero_job() # 1 MINUTOS e 6 SEGUNDOS
  time.sleep(18) # 28 segundos
  # 1h 13m
  refresh_hero() # 12 segundos
  time.sleep(120) # 2 minutos
  open_trunk() # 12 segundos
  time.sleep(120) # 2 minutos
  refresh_hero() # 12 segundos
  time.sleep(120) # 2 minutos
  open_trunk() # 12 segundos
  time.sleep(120) # 2 minutos
  refresh_hero() # 12 segundos
  time.sleep(120) # 2 minutos
  open_trunk() # 12 segundos
  time.sleep(120) # 2 minutos
  refresh_hero() # 12 segundos
  time.sleep(120) # 2 minutos
  open_trunk() # 12 segundos
  time.sleep(36) # 36 segundos

# 1 HORA 30 MINUTOS
def stage_two():
  play_space_crypto() # 4 MINUTOS e 10 SEGUNDOS
  play_hero_job() # 1 MINUTOS e 6 SEGUNDOS
  not_afk_bomb() # 22 MINUTOS
  close_space_game(); # 10 SEGUNDOS
  not_afk_bomb() # 22 MINUTOS
  play_hero_job() # 1 MINUTOS e 6 SEGUNDOS
  not_afk_bomb() # 22 MINUTOS
  refresh_hero() # 12 segundos
  time.sleep(120) # 2 minutos
  open_trunk() # 12 segundos
  time.sleep(84) # 1 minuto e 24 segundos
  refresh_hero() # 12 segundos
  time.sleep(120) # 2 minutos
  open_trunk() # 12 segundos
  time.sleep(120) # 2 minutos
  refresh_hero() # 12 segundos
  time.sleep(120) # 2 minutos
  open_trunk() # 12 segundos
  time.sleep(120) # 2 minutos
  refresh_hero() # 12 segundos
  time.sleep(120) # 2 minutos
  open_trunk() # 12 segundos
  time.sleep(120) # 2 minutos
  refresh_hero() # 12 segundos
  time.sleep(16) # 16 segundos

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
        play_bot_bomb() # 47 minutos e 6 segundo
    
    if select == 2:
      while True:
        play_bot_luna() # 4 horas 42 minutos e 40 segundos

    if select == 3:
      while True:
        play_bot_space() # 24 minutos e 20 segundos

    if select == 5:
      while True:
        os.system('cls' if os.name == 'nt' else 'clear') # limpar console
        print('############### FASE 1 ###############')
        stage_one() # 1h 30m
        print('############### FASE 2 ###############')
        stage_two() # 1h 30m
        print('############### FASE 3 ###############')
        stage_two() # 1h 30m
        print('############### RESETAR FASES ###############')
main_menu()