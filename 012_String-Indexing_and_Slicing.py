# ---------------------------------
# Strings Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
# ---------------------------------

# Indexing ( Access Single Item )

myString = "I love python"

print(myString[0])
print(myString[9])

print(myString[-1])
print(myString[-6])

# Slicing ( Access Multiple Sequence Items)

print(myString[8:11])
print(myString[3:5])

print(myString[:10])
print(myString[5:])
print(myString[:])

print(myString[0::1])
print(myString[::1])

print(myString[0::2])
print(myString[0::3])
