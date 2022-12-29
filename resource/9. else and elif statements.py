# elif is short form of else if statement
# elif is used to check if the first statement isnt true, then program checks if the elif statement is true
# if and Elif statements always ends with :
# else statement is triggered when none of the if or elif statement is true

def check_age():

    age = input("Please enter your age: ")
        
    if age == 18:
        print("You are an adult")

    elif age >= 12:
        print("You are a child")

    else:
        print("You are baby")

    return check_age()



