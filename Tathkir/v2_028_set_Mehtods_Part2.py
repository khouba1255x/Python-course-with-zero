# -----------------
# -- Set Methods --
# -----------------

# difference()

a = {1, 2, 3, 4}
b = {1, 2, 3, "Osama", "Ahmed"}

print(a)
print(a.difference(b))
print(a - b)
print(a)

print("=" * 40)
# difference_update()

c = {1, 2, 3, 4}
d = {1, 2, 3, "Osama", "Ahmed"}
print(c)
c.difference_update(d)       
print(c)

print("=" * 40)
# intersection()

e = {1, 2, 3, 4, "X"}
f = {"Osama", "X", 2}
print(e)
print(e.intersection(f))
print(e & f)
print(e)

print("=" * 40)
# intersection_update()

g = {1, 2, 3, 4, "X", "Osama"}
h = {"Osama", "X", 2}
print(g)
g.intersection_update(h)
print(g) 

print("=" * 40)
# symmetric_diffenrence()

i = {1, 2, 3, 4, 5, "X"}
j = {"Osama", "Zero", 1, 2, 4}
print(i)
print(i.symmetric_difference(j))
print(i)

print("=" * 40)
# symmetric_diffenrence_update()

k = {1, 2, 3, 4, 5, "X"}
l = {"Osama", "Zero", 1, 2, 4}
print(k)
k.symmetric_difference_update(l)
print(k)