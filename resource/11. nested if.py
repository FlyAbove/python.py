# you can put an if statement in another else, if or elif statement, in short if statements inside other if statements, so called nested if statements


mark =  input("Input your marks")

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