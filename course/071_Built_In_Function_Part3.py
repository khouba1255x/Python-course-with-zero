# ------------------------
# -- Built In Functions --
# ------------------------
# abs()
# pow()
# min()
# max()
# slice()
# ------------------------

print("=" * 40)
# abs()
print("# abs()")
 
print(abs(100))
print(abs(-100))
print(abs(10.19))
print(abs(-10.19))

print("=" * 40)
# pow (base, exp, mod ) => Power 
print("# pow (base, exp, mod ) => Power ")

print(pow(2, 5))
print(pow(2, 5, 10))

print("="  * 40)
# min (item, item, item or iterator)
print("# min (item, item, item or iterator)")

myNumbers = (1, 20, -50, -100, 100)
print(min(1, 10, -50, 20, 30))
print(min("A", "X", "Z", "Osama"))
print(min(myNumbers))

print("=" * 40)
# max (item, item, item or iterator)
print("# max (item, item, item or iterator)")

myNumbers = (1, 20, -50, -100, 100)
print(max(1, 10, -50, 20, 30))
print(max("A", "X", "Z", "Osama"))
print(max(myNumbers))

print("=" * 40)
#slice(star, end, step)
print("#slice()")

a = ["A", "B", "C", "D", "E", "F"]

print(a[:5])
print(a[slice(5)])
print(a[slice(2, 5)])
