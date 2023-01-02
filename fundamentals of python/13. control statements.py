# In Python, Loops are used to iterate repeatedly over a block of code
# In order to change the way a loop is executed from its usual behavior, control statements are used
# Control statements are used to control the flow of the execution of the loop based on a condition

# The statement in Python is used to terminate or abandon the loop containing the statement and brings the control out of the loop
# It is used with both the while and the for loops, especially with nested loops (loop within a loop) to quit the loop
# It terminates the inner loop and control shifts to the statement in the outer loop

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")

else:
    print("You are not eligible to vote")
