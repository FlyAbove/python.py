import random

def get_choices():

    player_choice = input("Choose rock paper or scissors") # This is value inputted from user
    options = ["rock", "paper", "scissors"] # This is our lists of options
    computer_choice = random.choice(options) # This uses random library to choose random item from our list
    choices = {"computer chosed": computer_choice, "player chosed": player_choice} #This is our dictionary of choices

    return choices # The function get_choices is going to return "choices" in console when function is called

choices = get_choices() # Here we mention variable choices as our function

# choices = {'computer chosed': computer_choice, 'player chosed': player_choice}
# So we need to learn how to access the element "player_choice" from this dictionary
# Remember player_choice is a variable but the input the user will provide is the element
# For example: computer chosed: "paper" player chosed "rock", so the rock and paper is our element and this is what we need to access from our dictionary

# To access value from dictionary

accessing_value = choices["computer chosed"]
print(f'We successfully accessed "{accessing_value}" key from our dictionary')

# So here we created a variable "accessing_value" which is the value of "computer chosed" key 
# The "choices" actually tells the program to access the choices dictionary and "computer chosed" is actually telling the program to access the "computer chosed" keyS