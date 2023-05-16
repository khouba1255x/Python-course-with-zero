# -----------------
# -- Set Methods --
# -----------------

# issuperset()

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b))
print(a.issuperset(c))

print("=" * 40)
# issubset()

d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}
print(d.issubset(e))
print(d.issubset(f))

print("=" * 40)
# isdisjoint()

g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}

print(g.isdisjoint(h))
print(g.isdisjoint(i))