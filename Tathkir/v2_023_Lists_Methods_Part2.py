# -------------------
# -- Lists Methods --
# -------------------

# clear()

a = [1, 2, 3, 4]
a.clear()
print(a)

print("=" * 40)
# copy()

b = [1, 2, 3, 4]
c = b.copy()

print(b)
print(c)

b.append(5)

print(b)
print(c)

print("=" * 40 )
# cont()

d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))

print("=" * 40)
# index()

e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))

print("=" * 40)
# insert()

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(7, "Test")
 
print(f)

print("=" * 40)
# pop() 

g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))
print(g)