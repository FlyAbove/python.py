 # Strings are any character written between " "
 
 # We can concatenate strings using + operator

string = "name"
string += "second name"

print(string)

# Another way to concatenate strings is written down below

name = "John"
last_name = "Smith"
full_name = name + " " + last_name

print(full_name)

# To concatenate strings with variables we use f strings
# The variable is enclosed in {} brackets 

name1 = "John"
full_name = f"My full name is {name1} Smith"

# We can create multi line strings using """ """ syntax

multi_string = """ 
I
am
a
good
boy
"""

print(multi_string)

# String-Methods

# To convert a string to lower or upper case, we use .lower() and .upper() respectively
# To convert first letter of each string to capital letter

print("LOWER".lower())
print("upper".upper())
print("tITLE cHARACTErs".title())

# All string methods that you can use on Python are written down below
# Note: Al string method returns new values. They do not change the original string


# capitalize() # Converts the first character to upper case
# casefold() # Converts string into lower case
# center() # Returns a centered string
# count() # Returns the number of times a specified value occurs in a string
# encode() # Returns an encoded version of the string
# endswith() # Returns true if the string ends with the specified value
# expandtabs() # Sets the tab size of the string
# find() # Searches the string for a specified value and returns the position of where it was found
# format() # Formats specified values in a string
# format_map() # Formats specified values in a string
# index()	# Searches the string for a specified value and returns the position of where it was found
# isalnum() # Returns True if all characters in the string are alphanumeric
# isalpha() # Returns True if all characters in the string are in the alphabet
# isascii() # Returns True if all characters in the string are ascii characters
# isdecimal()	# Returns True if all characters in the string are decimals
# isdigit() # Returns True if all characters in the string are digits
# isidentifier() # Returns True if the string is an identifier
# islower() # Returns True if all characters in the string are lower case
# isnumeric() # Returns True if all characters in the string are numeric
# isprintable() # Returns True if all characters in the string are printable
# isspace() # Returns True if all characters in the string are whitespaces
# istitle() # Returns True if the string follows the rules of a title
# isupper() # Returns True if all characters in the string are upper case
# join() # Converts the elements of an iterable into a string
# ljust() # Returns a left justified version of the string
# lower() # Converts a string into lower case
# lstrip() # Returns a left trim version of the string
# maketrans() # Returns a translation table to be used in translations
# partition() # Returns a tuple where the string is parted into three parts
# replace() # Returns a string where a specified value is replaced with a specified value
# rfind() # Searches the string for a specified value and returns the last position of where it was found
# rindex() # Searches the string for a specified value and returns the last position of where it was found
# rjust() # Returns a right justified version of the string
# rpartition() # Returns a tuple where the string is parted into three parts
# rsplit() # Splits the string at the specified separator, and returns a list
# rstrip() # Returns a right trim version of the string
# split() # Splits the string at the specified separator, and returns a list
# splitlines() # Splits the string at line breaks and returns a list
# startswith() # Returns true if the string starts with the specified value
# strip() # Returns a trimmed version of the string
# swapcase() # Swaps cases, lower case becomes upper case and vice versa
# title() # Converts the first character of each word to upper case
# translate() # Returns a translated string
# upper() # Converts a string into upper case
# zfill() # Fills the string with a specified number of 0 values at the beginning

# We going to use is and in operators

name = "John"
check = "oh" in name # in operator is case sensitive
print(check)

check_2 = "John" is name # is operator is case sensitive
print(check_2)
