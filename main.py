import os
import Player
# from playsound import playsound
import winsound
intro_message = """
**************************************************************************************
* Welcome, stranger.
* Here in Hinderlands, you'll get to fight dragons and conquer the deadliest dungeons.
* In a country where magic rules, anything is possible if you wish so.
* It all depends on you, brave hero.
**************************************************************************************
"""
sound = "Main_Menu.wav"
winsound.PlaySound(sound,winsound.SND_ASYNC)
print(intro_message)
print("Play ? Yes or No")
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
        path_option = input("""1.Village
2. Forest
3. Desert
Choose your place. :""")
    elif class_select == '2':
        player_name = input('What is your name?: ')
        player = Player.Wizard
    else:
        print('Choose a valid option.')
else:
    print('Thank you, goodbye.')