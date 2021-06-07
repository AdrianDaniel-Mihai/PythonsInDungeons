import os
intro_message = """
**************************************************************************************
* Welcome, stranger.
* Here in Hinderlands, you'll get to fight dragons and conquer the deadliest dungeons.
* In a country where magic rules, anything is possible if you wish so.
* It all depends on you, brave hero.
**************************************************************************************
"""
print(intro_message)
print("Play ? Yes or No")
user_response = input('Yes or No?:')
if user_response.upper() == 'YES':
    print('Let the game begin!')
    os.system('cls')
else:
    print('Thank you, goodbye.')