# -----------------
# -- Set Methods --
# -----------------

# clear()
print("clear()   :")

a = {1, 2, 3}
a.clear()
print(a)

# union()
print("union()   :")

b = {"One", "Tow", "Three"}
c = {"1", "2", "3"}
x = {"Zero", "Cool"}

print(b | c)
print(b.union(c, x))

# add()
print("add()   :")

d = {1, 2, 3, 4}
d.add(6)
d.add(5)
print(d)

# copy()
print("copy()   :")

e = {1, 2, 3, 4}
f = e.copy

print(e)
print(f)

e.add(6)

print(e)
print(f)

# remove()
print("remove()   :")

g = {1, 2, 3, 4}
g.remove(1)
# g.remove(7)   # error
print(g)

# discard()
print("discard()   :")

h = {1, 2, 3, 4}
h.discard(1)
h.discard(7)
print(h)

# pop()
print("pop()   :")

i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())

# update()
print("update()   :")

j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(["Html", "Css", 1])
j.update(k)

print(j)
