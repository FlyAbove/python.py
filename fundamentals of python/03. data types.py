# A variable can store multiple types of data 
# Python supports following types of data 
# int, float, complex, list, tuple, range, dict, set, frozenset, bool, bytes, bytearray, memoryview, NoneType

# Some valid examples of different types of data that can be stored in a variable are written down below

a = "Hello" # Data type = string
b = 1 # Data type = integer
c = 3.0 # Data type = float
d = 1j # Data type = complex
e = ["python", "javascript", "c++"] # Data type = list
f = ("python", "javascript", "c++") # Data type = tuple
g = {"python", "javascript", "c++"} # Data type = set
h = frozenset({"python", "javascript", "c++"}) # Data type = frozenset
i = True # Data type = boolean
j = b"Hello" # Data type = bytes
k = bytearray(1) # Data type = bytearray
l = memoryview(bytes(5)) # Data type = memoryview
m = None # Data type = NoneType
n = {"lang": "python"} # Data type = dictionary

# You can get the data type of any object by using type() function

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(n))

# We can olso check if any variable is string, list, int, float etc

print(type(a) == str)
print(type(b) == int)
print(type(c) == float)
print(type(d) == complex)
print(type(e) == list)
print(type(f) == tuple)
print(type(g) == set)
print(type(h) == frozenset)
print(type(i) == bool)
print(type(j) == bytes)
print(type(k) == bytearray)
print(type(l) == memoryview)
print(type(n) == dict)
