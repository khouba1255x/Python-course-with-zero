# -----------
# -- Tuple --
# -----------

# Tuple With One Element
print("# Tuple With One Element")

myTuple1 = ("Osama")
myTuple2 = "Osama"

print(myTuple1)
print(myTuple2)

print(type(myTuple1))
print(type(myTuple2))

# Tuple Concatenation
print("# Tuple Concatenation")

a = (1, 2, 3, 4)
b = (5, 6)

c = a + b
d = a + ("A", "B", True)

print(c)
print(d)

# Tuple, List, String Repeat (*)
print("# Tuple, List, String Repeat (*)")

myString = "Osama"
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)
print(myList * 6)
print(myTuple * 6)

# Methods => count()
print("# Methods => count()")

a = (1, 3, 7, 8, 2, 6, 5, 8)
print(a.count(8))

# Mehtods => index()
print("# Mehtods => index()")

b = (1, 3, 7, 8, 2, 6, 5)
# print("The Position of Index is :" + b.index(7)) # Error
print("The Position of Index is : {:d}".format(b.index(7)))
print(f"The Position of Index is : {b.index(7)}")

# Tuple Destruct
print("# Tuple Destruct")

a = ("A", "B", 4,  "c")

x, y, z = "A", "B",  "C"
print(x)
print(y)
print(z)

x, y, _, z = a
print(x)
print(y)
print(z)
