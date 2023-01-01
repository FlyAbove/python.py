# Boolean values are True and False, these are case sensitive
# If a value is not Boolean we have some rules depending on the data type 
# For example numbers are always true except the number 0
# Strings, lists, tuple, sets and dictionary are always true except empty strings, lists, tuple, sets and dictionary
# Note: Strings with space is not considered as an empty string

# Some boolean operations are written down below

name = True # Change True to False and check how program runs itself

if name:
    print("true1")

else:
    print("false1")

name2 = "" # An empty string

if name2:
    print("true2")

else:
    print("false2")

name3 = " " # Not an empty string

if name3:
    print("true3")

else:
    print("false3")

# any and all functions are very usefull for boolean expressions

# Some valid expressions are written down below

eggs = True
milk = False

cake = any([eggs, milk]) # any iterable returns value True when one of the value is True
print(cake)

cheeze = True
dough = False

pizza = all([cheeze, dough, ]) # all iterable returns value True when all of the value is True
print(pizza)