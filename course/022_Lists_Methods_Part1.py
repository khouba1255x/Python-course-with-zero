# -------------------
# -- Lists Methods --
# -------------------

# append()

myFriends = ["Osama", "Ahmed", "Sayed"]
myOldFriends = ["Haytham", "Samah", "Ali"]

myFriends.append("Alaa")
myFriends.append(100)
myFriends.append(150.200)
myFriends.append(True)
myFriends.append(myOldFriends)


print(myFriends)
print(myFriends[2])
print(myFriends[6])
print(myFriends[7])
print(myFriends[7][2])

# extend()
print("extend")

a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)

print(a)

# remove()
print("#remove()")

x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
x.remove("Osama")
print(x)

# sort()
print("#sort()")

# y = [1, 2, 100, 120, -10, 17, 29]
y = ["A", "Z", "C"]
print(y)
y.sort(reverse=True)
print(y)

# reverse()
print("#reverse()")

z = [10, 1, 9, 80, 100, "Osama", 100]
z.reverse()
print(z)
