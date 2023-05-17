print("=" * 40)
# 1 : 
print("assignment 1: ")

name = "Osama",

print(name)
print(type(name))

print("=" * 40)
# 2 :
print("assignment 2: ")

print("=" * 10)
# type 1 :
print("type 1 :")

friends = ("Osama", "Ahmed", "Sayed")

print(friends)

friends = ("Elzero", "Ahmed", "Sayed")
print(friends)
print(len(friends),"Elements")

print("=" * 10)
# type2 :
print("type 2 :")

friends = ("Osama", "Ahmed", "Sayed")

print(friends)

name = "Elzero",

friends = name + friends[1:]
print(friends)
print(len(friends),"Elements")

print("=" * 40)
# 3 :
print("assignment 3 : ")

print("=" * 10)
# type 1 : 
print("type 1:")

num = (1, 2, 3)
letters = ("A", "B", "C")

t = num + letters

print("nums and letters one",t)
print(len(t), "Elements")

print("=" * 10)
# type 2 : 
print("type 2:")

num = (1, 2, 3)
letters = ("A", "B", "C")

print(num + letters)
print(len(num + letters), "Elements")

print("=" *40)
# 4 :
print("assignment 4: ")

my_typle = (1, 2, 3, 4)

a, b, _, c = my_typle

print(a)
print(b)
print(c)