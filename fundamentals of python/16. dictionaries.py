# Dictionaries allow you to create key value pairs

# Some valid examples of dictionaries are written down below

dictionary = { "school": "idk", "name": "John", "grade": 10, 7: "int", ("tuple"): "tuple" }
print(dictionary)

# If you need to print a value of a key we use print(dict_name["key_name"]) or dict_name.get("key")

print(dictionary["school"])
print(dictionary.get("grade"))

# To remove and return last key value pair in a dictionary we use .popitem()

print(dictionary.popitem())

# To check if a key exists in any of the dictionary we use in function

if "name" in dictionary:
    print(f"Key called name is present in dictionary")

else:
    print("sorry")

# We can olso modify the value of a key in a dictionary

dictionary['name'] = input("Enter your name: ")
print(dictionary['name'])
