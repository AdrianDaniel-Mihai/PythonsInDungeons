import os
import Player
import Enemy
import winsound
import Utils
import random

print(Utils.intro_message)
sound = "Main_Menu.wav"
winsound.PlaySound(sound, winsound.SND_ASYNC)

print(Utils.play_choice)
user_response = input(Utils.user_response)
if user_response.upper() == 'YES':
    print('Let the game begin!')
else:
    print('Thank you. Bye-Bye')
    quit()
    os.system('cls')
class_select = input(Utils.class_select)
player_name = input('Your name?\nName: ')
sound = 'Exploring.wav'
winsound.PlaySound(sound, winsound.SND_ASYNC)

if class_select == '1':
    player = Player.Warrior
elif class_select == '2':
    player = Player.Wizard
else:
    print('Choose a valid option.')


path_option = input(Utils.path_option)
if path_option == '1':
    print(Utils.village_start)
    sound = 'BattleFinal.wav'
    winsound.PlaySound(sound, winsound.SND_ASYNC)
    random_number = random.randint(0, 2)
    if random_number == 0:
        enemy = Enemy.Goblin()
        print('Damn these goblins.')
        input('Press a key to continue')
    elif random_number == 1:
        enemy = Enemy.Orc()
        print('Orcs never learn...')
        input('Press a key to continue')
    elif random_number == 2:
        enemy = Enemy.Rat()
        print('Want some cheese?RAT-atouille?')
        input('Press a key to continue')
if path_option == '2':
    print(Utils.forest_start)
    sound = 'BattleFinal.wav'
    winsound.PlaySound(sound, winsound.SND_ASYNC)
    random_number = random.randint(0, 2)
    if random_number == 2:
        enemy = Enemy.Rat()
        print('Want some cheese?RAT-atouille?')
        input('Press a key to continue')
    elif random_number == 0:
        enemy = Enemy.Goblin()
        print('Damn these goblins.')
        input('Press a key to continue')
    elif random_number == 2:
        enemy = Enemy.Orc()
        print('Orcs never learn...')
        input('Press a key to continue')
if path_option == '3':
    print(Utils.desert_start)
    enemy = Enemy.Scorpion()
    print('This is not MK, get back Scorpion.')
    input('Press a key to continue')
    enemy.atack()
else:
    print('Path not available.')
