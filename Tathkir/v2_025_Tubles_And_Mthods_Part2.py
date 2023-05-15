# -----------
# -- Tuple --
# -----------

# Tuple With One Element :
 
myTuple1 = ("Osama",)
myTuple2 = "Osama",

print(myTuple1)
print(myTuple2)

print(type(myTuple1))
print(type(myTuple2))

print(len(myTuple1))
print(len(myTuple2))

print("=" * 40)
# Tuple Concatenation 

a = (1, 2, 3, 4)
b = (5, 6)

c = a + b
d = a + ("A", "B", True) + b 

print(c)
print(d)

print("=" * 40)
# Tuple, List, Strig Repeat (*) 

myString = "Osama"
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)
print(myList * 6)
print(myTuple * 6)

print("=" * 40)
# Methods => count()

a = (1, 3, 7, 8, 2, 6, 5, 8)
print(a.count(8))

print("=" * 40)
# Methods => index()

b = (1, 3, 7, 8, 2, 6, 5)
print("The Positon of index is :",b.index(7))
print("The Positon of index is : {:d}".format(b.index(7)))
print(f"The Positon of index is : {b.index(7)}")

print("=" * 40)
# Tuple Destruct 

a = ("A", "B", 4, "C")

x, y, z = "A", "B", "C"

print(x)
print(y)
print(z)

print("=" * 40)

x, y,_, z = a

print(x)
print(y)
print(z)
