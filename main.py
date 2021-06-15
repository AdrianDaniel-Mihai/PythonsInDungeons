import os
import Player
import Enemy
import winsound
import Utils
import random
print(Utils.intro_message)
sound = "Main_Menu.wav"
winsound.PlaySound(sound, winsound.SND_ASYNC)

print("Do you want to play ? Yes or No")
user_response = input('Yes or No?:')
if user_response.upper() == 'YES':
    print('Let the game begin!')

    os.system('cls')
    class_select = input('What type of player are you?\n'
          '1 for Warrior, 2 for Wizard:')

    if class_select == '1':
        player_name = input('What is your name?: ')
        player = Player.Warrior
        sound = 'Exploring.wav'
        winsound.PlaySound(sound, winsound.SND_ASYNC)
        path_option = input("""1. Village
2. Forest
3. Desert
Choose your place. :""")
        if path_option == '1':
            #in_village from utils
            print('You are in the village.')
            print('From a backside alley, an enemy appears')
            sound = 'BattleFinal.wav'
            winsound.PlaySound(sound, winsound.SND_ASYNC)
            random_number = random.randint(0,2)
            if random_number == 0:
                enemy = Enemy.Goblin()
                input('Press a key to continue')
            elif random_number == 1:
                enemy = Enemy.Orc()
                input('Press a key to continue')
            elif random_number == 2:
                enemy = Enemy.Rat()
                input('Press a key to continue')


        elif path_option == '2':
            print('You are in the forest.')
        elif path_option == '3':
            print('You are in the desert.')
        else:
            print('Path not available.')
    elif class_select == '2':
        player_name = input('What is your name?: ')
        player = Player.Wizard
    else:
        print('Choose a valid option.')
else:
    print('Thank you, goodbye.')

    # continuam libraria utils si curatam codul