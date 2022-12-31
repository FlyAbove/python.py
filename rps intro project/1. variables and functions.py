# variables and functions
def get_choices(): # def = defines function, "get_choices" = function name, function always ends with ():
  
    player_choices = "rock" # "player_choices" is variable name, "rock" is variable data as in string
    computer_choices = "paper"

    return computer_choices # Returning variable when function is called

choices = get_choices() # Assigning function as a variable
print(choices) # Printing variable which is assigned as a function
