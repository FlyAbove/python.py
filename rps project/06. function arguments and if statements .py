# Now you already know how to create a function
# Now to check that who won our rock paper or scissors game we need to create function arguments 

def check_winner(player, computer): # Player and computer are two variables
  if player == computer: # Double == shows that two arguements are equals, if we used one = it would be incorrect because one = assigns value to a variable
    return ("Both arguments are same") # The program is going to return statement in console only if the "if" statements is correct

# Parentheses are optional in return statement, return "Text"
# The space before if shows that "if" is intented in function "check_winner" whereas space before return shows that "return" is intented in "if" statement
