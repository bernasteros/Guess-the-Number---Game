from art import logo
from random import randint


def number_pick():
    """Selects a random number between 1 and 100"""
    secret_number = randint(1, 100)

    return secret_number

def difficulty():
    """The choice is picking a amount of attempts the player is allowed to make"""
    choice = ""
    level_dict = {
     "easy": 10,
     "hard": 5,
     "lottery":1,
     }
    
    choice = input('''Please choose a level:
    "easy" = 10 tries
    "hard" = 5 tries
    "lottery" = 1 try
    > ''').lower()

    while choice not in level_dict:
        input("Please enter a valid level: ").lower()
      
    return level_dict[choice]

print(logo)
