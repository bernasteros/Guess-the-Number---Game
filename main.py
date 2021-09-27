from art import logo
from random import randint
from os import name, system

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def number_pick():
    """Selects a random number between 1 and 100"""
    secret_number = randint(1, 100)

    return secret_number

def difficulty():
    """The choice is picking a amount of attempts the player is allowed to make"""

    clear()
    print(logo)
    
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
        choice = input("Please enter a valid level: ").lower()

    choice = level_dict[choice]  
    return choice

def guess_number(solution, life):
    my_number = 0

    while my_number != solution:
        
        try:
            my_number = int(input("Guess the number:"))
        except TypeError:
            print("Error: This is no word-guessing game!")
        clear()
        print(logo)
        if my_number == solution:
            print("Congratulations, you found the number!")
        else:
            life -= 1
            if life == 0:
                print(f"Game Over!\n The solution was {solution}")
                break
            else:
                if my_number > solution:
                    print(f"The number is lower than your guess.\n Attempts remaining: {life}")
                else:
                    print("The number is higher than your guess.\n Attempts remaining: {life}")

print(logo)

while input("Start a new game? (y/n)").lower() == "y":
    life = difficulty()
    guess_number(number_pick(), life)