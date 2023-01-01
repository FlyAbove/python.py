# Libraries help your program do certain features without programming them yourself
# Usually written on the top of your file
# To import a library we use import "library name"


# Now we are going to try create a program which will allow computer to play rps without pre defined variable

import random

def get_choices():

    player_choice = input("Choose one of the following (rock, paper or scissors) : ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    choices = {"player chosed": player_choice, "computer chosed": computer_choice}

    return choices

choices = get_choices()
print(choices)
