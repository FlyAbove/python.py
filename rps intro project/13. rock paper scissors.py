# So after reading all of the files, you should be able to make a rock paper scissors game
# Here is an example of how you can make one
# It's recommended to try to create a game on your own first

import random

def get_choices():

    player_choice = input(" Choose one of the following (rock, paper or scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"Computer chosed:": computer_choice, "Player chosed:": player_choice}

    return choices

choices = get_choices()
print(choices)

def check_win(player, computer):
    print(f"You choosed {player} and computer choosed {computer}")

    if player == computer:
        return "It's a tie! "

    elif player == "rock":
        if computer == "scissors":
                return "You won!"
    
    elif player == "scissors":
        if computer == "rock":
                return "You loose"

    elif player == "rock":
        if computer == "scissors":
                return "You won!"

    elif player == "scissors":
        if computer == "rock":
                return "You won!"

    result = check_win(choices["player"], choices["computer"])
    print(result)

    

        