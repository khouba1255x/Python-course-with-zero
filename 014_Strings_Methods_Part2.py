# ---------------------
# -- Strings Methods --
# ---------------------

# split() rsplit()

a = "I Love Python and PHP and MySQL"
print(a.split())

b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))

c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split("-", 4))

d = "I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit("-", 4))

# center()

e = "Osama"
print(e.center(9))
print(e.center(9, "#"))
print(e.center(15, "@"))

# count()

f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))
print(f.count("PHP", 0, 25))

# swapcase()

g = "I Love Python"
h = "i loVE pYTHON"

print(g.swapcase())
print(h.swapcase())

# startswith()

i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("P", 7, 12))

# endswith()

j = "I Love Python"
print(j.endswith("n"))
print(j.endswith("S"))
print(j.endswith("e", 2, 6))
