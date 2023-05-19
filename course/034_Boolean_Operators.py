# -----------------------
# -- Boolean Operators --
# -----------------------
# and
# or
# not
# -----------------------

age = 36
country = "Egypt"
rank = 10

print("=" * 10)

print(age > 3)
print(country == "KSA")

print("=" * 10)

print(age > 16 and country == "Egypt" and rank > 0 )
print(age > 16 and country == "Egypt" and rank > 11 )

print("=" * 10)

print(age > 16 or country == "Egypt")
print(age > 16 or country == "KSA")
print(age > 46 or country == "KSA")

print("=" * 10)

print(age > 16)
print(not age > 16) # Not True = False