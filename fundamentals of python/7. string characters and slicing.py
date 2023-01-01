# As strings are array of bytes stored in variables, hence they are bits of data 
# We can access a character from string using string_name[number of the character]
# If we need to access character(s) between two characters, this is called string slicing

# Some valid examples of accessing characters from a string is written down below

# Note: the first character of the string is indexed as number 0, to access letter "p" in pizza we need to write food[0]

food = "pizza"
print(food[1])

# In slicing we specify the range, 0:4 tells Python to access characters starting from index 0 and ending before index 4
# In slicing the number 4 olso tells how many number of characters will be printed, in this case the number 4 equals to 4 characters

print(food[0:4])