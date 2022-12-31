# Operators are used to perform operations on variables and values
# Python divides operators in the following groups
# Arithmetic operators, Assignment operators, Comparison operators, Logical operators, Identity operators, Membership operators, Bitwise operators

# Arithmetic operators are used with numeric values to perform common mathematical operations

# Some valid arithmetic operations are written down below

a + b # Addition operation, + represents addition operator
a - b # Subtraction operation, - represents subtraction operator
a * b # Multiply operation, * represents multiplication operator
a / b # Divide operation, / represents division operator
a % b # Modulus operation, % represents modulus operator
a **b # Expotention operation, ** represents exponent operator
a //b # FLOOR division operation, // represents floor division operator

# Assignment operators are used to assign values to variables that

# Some valid assignment operations are written down below

a = b # Assignment operation, = assigns values to variables 
a += b # Add and equal to operator
a -= b # Subtract and equal to operator
a *= b # Aterisk and equal to operator
a /= b # Divide and equal to operator
a %= b # Modulus and equal to operator
a //= b # Double divide and equal to operator
a **= b # Exponent assign and equal to operator
a &= b # Bitwise and equal to operator
a |= b # Bitwise and equal to operator
a ^= b # Bitwise XOR assignment operator
a >>= b # Bitwise right shift operator
a <<= b # Bitwise left shift operator

# Logical operators are used to combine conditional statements

# Some valid logical operations are written down below

a < 15 and b > 10 # Returns True if both statements are true
a < 15 or b > 10 # Returns True if one of the statements are true
not(a < 15 and b > 10) # Reverse the results, returns False if the statement is True

# Identity operators are used to compare objects, not if they are equal, but if they are actually the same object, with the same memory location

# Some valid identity operations are written down below

a is b # Returns True if both variables are the same object
a is not b # Returns true if both variables are not the same object

# Membership operators are used to test if a sequence is presented in an object

# Some valid membership operations are written down below

a in b # Returns True if a sequence with the specified value is present in the object
a not in b # Returns True if a sequence with the specified value is not present in the object

# Bitwise operators are used to compare binary numbers 

# Bitwise operators are written down below

# & = AND operator, sets each bits to 1 if both bits are 1
# | = OR operator, sets each bits to 1 if one of two bits is 1
# ^ = XOR operator, sets each bit to 1 if only one of two bits is 1
# ~ = NOT, Inverts all bits
# << = Zero fill left shift, shift left by pushing zeros in from the right and let the leftmost bits fall off
# >> = Signed right shift, shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off