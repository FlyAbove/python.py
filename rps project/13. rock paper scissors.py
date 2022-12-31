# So after reading all of the files, you should be able to make a rock paper scissors game
# Here is an example of how you can make one
# It's recommended to try to create the game on your own first

import random

def get_choices(): # Learn from variables and functions.py file 

    player_choice = input(" Choose one of the following (rock, paper or scissors): ")  # Learn from input.py file
    options = ["rock", "paper", "scissors"] # Learn from lists.py file
    computer_choice = random.choice(options) # Learn from libraries.py file
    choices = {"Computer chosed:": computer_choice, "Player chosed:": player_choice} # Learn from dictionary.py file

    return choices


def check_win(player, computer): 
    print(f"You choosed {player} and computer choosed {computer}") # Learn from f strings.py file

    if player == computer: # Learn from nested if.py file
        return "It's a tie! "

    elif player == "rock": # Learn from else and elif statements.py file
        if computer == "scissors":
                return "You won!"
    
        else:
            return "You loose"
    
    elif player == "scissors":
        if computer == "paper":
                return "You won"
        
        else:
            return "You loose"

    
    elif player == "paper":
        if computer == "rock":
                return "You won!"

        else:
            return "You loose"


choices = get_choices()
result = check_win(choices["Player chosed:"], choices["Computer chosed:"]) # Learn from accessing dictionary values.py
print(result)

    

        