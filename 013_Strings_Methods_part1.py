# ---------------------
# -- Strings Methods --
# ---------------------


a = "I Love Python"
b = "     I Love Python    "
print(len(a))
print(len(b))

# strip() rstrip() lstrip()
A = "    I Love Python     "
print(A.strip())
print(A.rstrip())
print(A.lstrip())

A = "####I Love Python#####"
print(A.strip("#"))
print(A.rstrip("#"))
print(A.lstrip("#"))

A = "###@@I Love Python#@#@@#"
print(A.strip("#@"))
print(A.rstrip("#@"))
print(A.lstrip("#@"))

# titile()
b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())

b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())

# zfill

c, d, e, f, = "1", "11", "111", "1111"

print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

# upper() , lower()

g = "osama"
print(g.upper())

h = "OSaMa"
print(h.lower())
