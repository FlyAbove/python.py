# Tuples is another data type in Python
# Tuples cannot be modified like lists or strings

# Some valid examples of Tuples are written down below

tuples = ("Bat", "Air")
print(tuples)

# We cannot use .sort() function to sort tuples because .sort() modifies the original data type but we cannot modify tuples
# In order to sort tuples we use sorted() function

sorting = ("Ball", "Cat", "Apple")
print(sorted(sorting))

# We can combine two tuples and create a new tuple but we cannot modify an existing one

newTuple = sorting + tuples 
print(sorted(newTuple))