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
