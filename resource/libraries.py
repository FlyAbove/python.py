# libraries help your program do certain features without programming them yourself
# usually written on the top of your file
# to import a library we use import "library name"


# now we are going to try create a program which will allow computer to play rps

import random

def get_choices():

    player_choice = input("Choose one of the following (rock, paper or scissors) : ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    choices = {"player chosed": player_choice, "computer chosed": computer_choice}

    return choices

choices = get_choices()
print(choices)
