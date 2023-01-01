# Enums are readable names bound to a constant value
# Enumerations in Python are implemented by using the module named "enum".
# Enumerations are created using classes. 
# Enums have names and values associated with them
# We use enums because there is no way to enforce a variable as constant in Python

# We need to import Enum from enum standard library module

from enum import Enum

class temperature(Enum):
    day = 20
    noon = 30
    night = 10
    car = "red"

print(temperature("red")) # This prints the enum member with value "red

print(temperature.day) # Printing enum as a string

print(temperature.noon.value) # Printing noon value using .value

print(type(temperature.noon.value)) # This prints type of the enum value 

print(type(temperature.noon)) # This prints the type of enum member

print(repr(temperature.noon)) # This returns the object representation in string format

print(list(temperature)) # This prints all enum members as a list