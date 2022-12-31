import random
def get_choices():

    player_choice = input("Choose rock paper or scissors") # This is value inputted from user
    options = ["rock", "paper", "scissors"] # This is our lists of options
    computer_choice = random.choice(options) # This uses random library to choose random item from our list
    choices = {'computer chosed': computer_choice, 'player chosed': player_choice} #This is our dictionary of choices

    return choices # The function get_choices is going to return "choices" in console when function is called



