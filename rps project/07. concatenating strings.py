# for concatenating strings you need to use + operator
# concatenating strings means to combine strings with other strings or variables

first_name = "John"
last_name = "Smith"
full_name = first_name+last_name 

# Printing like this doesnt provide us a space between our first and last name

print(full_name)

# To have space between our first and last names we need to concatenate an empty string with a space with a space between


first_name = "Michael"
last_name = "James"
full_name = first_name + " " + last_name # " " This is an empty string with space between

print(full_name)

# To concatenate more than two strings

a = "Iam" + " " + "a good" + " " + "boy"
print(a)
