def get_choices(): # we created a function and then called it on 8th line
    player_choice = input("Enter a choice = rock paper or scissors: ") # this variable is to be inputted by user
    computer_choice = "paper" # pre defined data as string
    choices = {"player": player_choice, "computer": computer_choice} # using dictionary to store player input data and variable data

    return choices

choices = get_choices()
print(choices)