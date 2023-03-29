# ---------------------
# -- Strings Methods --
# ---------------------

# index(SubString, Start, End)

a = "I Love Python"
print(a.index("P"))
print(a.index("P", 0, 10))
# print(a.index("P", 0, 5))

# find(SubString, Start, End)

b = "I Love Python"
print(b.find("P"))
print(b.find("P", 0, 10))
print(b.find("P", 0, 5))

# rjust(widht, Fill Char) ljudt(widht, Fill Char)

c = "Osama"
print(c.rjust(10))
print(c.rjust(10, "#"))

d = "Osama"
print(d.ljust(10))
print(d.ljust(10, "#"))

# splitlines()

e = """First Line 
Second Line
Third Line"""

print(e.splitlines())

f = "Fisrst Line\nSecond Line\nThird Line"
print(f.splitlines())

# expandtabs()

g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(5))


one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

three = " "
four = ""
print(three.isspace())
print(four.isspace())

five = "i love python "
six = "I Love Python "
print(five.islower())
print(six.islower())

seven = "osama_elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero100"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaaaaBbbbb"
y = "AaaaaaaaBbbbb111"
print(x.isalpha())
print(y.isalpha())

u = "AaaaaaaaBbbbb"
z = "AaaaaaaaBbbbb111"
print(u.isalnum())
print(z.isalnum())
