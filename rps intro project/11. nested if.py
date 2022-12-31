# A nested if statement is an if statement that is nested (meaning, inside) another if statement or if/else statement

mark = 80 # Change the numbers and check how program executes itself

if mark >= 60 and mark <= 100:
    if mark >= 90:
        print("You are the best!")
    elif mark >= 80:
        print("Well done!")
    elif mark >= 70:
        print("You can do better.")
    else:
        print("Pass.")
elif mark > 100:
    print("This mark is too high.")
elif mark < 0:
    print("This mark is too low.")
else:
    print("Failed.")