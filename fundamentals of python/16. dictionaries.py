# Dictionaries allow you to create key value pairs

# Some valid examples of dictionaries are written down below

dictionary = { "school": "idk", "name": "John", "grade": 10, 7: "int", ("tuple"): "tuple" }
print(dictionary)

# If you need to print a value of a key we use print(dict_name["key_name"])

print(dictionary["school"])
print(dictionary.get("grade"))


# We can olso modify the value of a key in a dictionary

dictionary['name'] = input("Enter your name: ")
print(dictionary['name'])