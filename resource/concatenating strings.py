# for concatenating strings you need to use + operator
# concatenating strings means to combine strings with other strings or variables

first_name = "John"
last_name = "Smith"
full_name = first_name+last_name 

# printing like this doesnt provide us a space between our first and last name

print(full_name)

# to have space between our first and last names we need to concatenate an empty string between two variables

first_name = "Michael"
last_name = "James"
full_name = first_name + " " + last_name

print(full_name)