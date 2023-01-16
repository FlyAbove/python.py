# Sets is a collection of data which is unordered, unchangeable and unindexed
# Set items are unchangeable, but you can remove items and add new items

# Some valid examples of sets are written down below

set1 = {"Home", "Shelby"}
set2 = {"Home", "Shelby", "Alpha"}

# Sets in maths can be intersected
# We use & to show intersection ∩ symbol in maths

intersection = set1 & set2 
print(intersection)

# We can take a union of sets like we take one in maths
# We use | symbol to show union U symbol in maths

union = set1 | set2 
print(union)

# We can take difference of two sets line we take on in maths

difference = set2 - set1
print(difference)

# We can take a subset of a set like we take one in maths
# We use > symbol to show subset ⊆ symbol in maths
# This shows that set1 contain all the elements of set2 

subset = set2 > set1
print(subset)

# We can check if elements of two sets are equal 

equal = set1 == set2
print(equal)


