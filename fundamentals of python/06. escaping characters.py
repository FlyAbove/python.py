# Escape character is a backlash \ followed by character you want to insert
# To insert characters that are illegal in string we use an escape character


# If you need to wrap any character in a string with "" 
# To do that we use \

name = "name \"wrapped\""
example = "\' wrapped"

print(name)
print(example)

# To add backslash in string we use \\

name1 = "backslash\\"
print(name1)

# To add new line without creating a multi line string we use \n

name2 = "new\nline"
print(name2)

# To delete last character/space in the string we use \b

name3 = "back \bspace" 
print(name3)
