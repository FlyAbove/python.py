# List is an important Python data structure
# Lists are used to store multiple value to a single variable 
# Lists can store different types of data to a single variable

# Some valid examples of lists are written down below

food = ['pizza', 'burger', 'bread', '']
empty_list = []
not_empty_list = [""]
different_data_type_list = ["string", 10, 10.7, 1+1j, food]

print(food)
print(len(empty_list))
print(len(not_empty_list))
print(different_data_type_list)

# To check if any value is in the list we use the in operator

print(1 in food) # Integer 1 is not in list named food, it is going to return False

# To access any value from the list by refrencing them by their indexes

print(food[0])

# You can olso update any value in a string by refrencing them by their indexes

update = ["1", "2", "4", "4"]

update[0] = 1
update[2] = "3"
slicing = update[0:3]

print(update)
print(slicing)

# There are two methods to add a value in a list without replacing the original value 1. append 2. extend
# Append method only takes one value as an argument

integers = [0, 1, 2, 3, 4]
integers.append(5)

# Extend is use to combine to lists, you can olso use += operator to function the same as an extend function

integers.extend([6, 7, 8, "End"])

print(integers)

plus = ["Buy", "me", "a"]
plus += ["coffee", "at", "www.buymeacoffee.com/flyabove"]

print(plus)

# We can add any value in a list at any specified index using .insert

items = ["please", "give", "to the repository"]
items.insert(2, "a star") # 2 specify the index in the list, "a star" is the value added at the specified index
print(items)

# We can remove any value from a list just like we can add one

remove = ["remove me", "leave me"]
remove.remove("remove me")
print(remove)

# We use .pop to return and remove the last item from the list

value = ["first value", "second value", "this value will be removed and returned"]
print(value.pop())

# To add multiple items in a list we use slicing

slicing = [1, 2, 3, 6]
slicing [3:3] = [4, 5] 
print(slicing)

# We can sort our lists using .sort()
# The list should contain only one data type
# Python sorts upper case letter first and then lower case

lists = ["Ball", "Bat", "Apple", "apple", "Dog" ] # Apple comes first as the letter A is the first alphabet
lists.sort()
print(lists)

# To ignore lower case and upper case sorting we use .sort(key = data_type.lower/upper)

lists.sort(key = str.upper)
print(lists)

