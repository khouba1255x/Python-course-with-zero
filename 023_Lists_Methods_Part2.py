# -------------------
# -- Lists Methods --
# -------------------

# clear()
print("# clear()")

a = [1, 2, 3, 4]
a.clear()
print(a)

# copy()
print("# copy()")

b = [1, 2, 3, 4]
c = b.copy()  # shallow copy of the list

print(b)
print(c)

b.append(5)

print(b)
print(c)

# count()
print("# count()")

d = [1, 2, 3, 4, 5, 1, 1, 5]
print(d.count(1))

# index()
print("# index()")

e = ["Osama", "Ahmed", "Sayed", "Ramy", "ahmed", "Ramy"]
print(e.index("Ramy"))

# insert()
print("# insert()")

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")
f.insert(-1, "Test")
print(f)

# pop()
print("# pop()")

g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))
