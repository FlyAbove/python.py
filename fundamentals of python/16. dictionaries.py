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

# We can get all keys and values from a dictionary using .keys() and values() functions respectively

keys = {"name": "John", "age": 18, "gender": "male"}

print(keys.keys())
print(keys.values())

# To convert every item in a dictionary into a list we used list(dict_name.items())

print(list(dictionary.items()))

# To add and delete a key value pair in dictionary

dictionary["key"] = "value"
print(dictionary)

del dictionary["grade"]
print(dictionary)

# To copy a dictionary we use .copy() function

newDictionary = dictionary.copy()
print(newDictionary)

# We can olso modify the value of a key in a dictionary

dictionary['name'] = input("Enter your name: ")
print(dictionary['name'])
