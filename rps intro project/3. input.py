def get_choices(): # We created a function and then called it on 8th line
    player_choice = input("Enter a choice = rock paper or scissors: ") # This variable is to be inputted by user
    computer_choice = "paper" # Pre defined data stored as string
    choices = {"player": player_choice, "computer": computer_choice} # Using dictionary to store player input data and variable data

    return choices 

choices = get_choices() # We created a variable called choices whose value is function "get_choices()" so we can print this variable 
print(choices) # Printing variable