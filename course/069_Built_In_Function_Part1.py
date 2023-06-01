# ------------------------
# -- Built In Functions --
# ------------------------
# all()
# any()
# bin()
# id()
# ------------------------
print("=" *40)

X = [1, 2, 3, 4, []]

if all(X) :
    print("Alll Elements Is True")

else :
    print("Theres At Least One Element Is False")

print("=" * 40)
X = [0, 0, 0, 0, []]

if any(X) :
    print("There's At Least One Element Is True")

else :
    print("There's No Any True Elements")

print("=" * 40)

print(bin(68))

print("=" * 40)

a = 1
b = 2

print(id(a))
print(id(b))