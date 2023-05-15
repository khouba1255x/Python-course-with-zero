# -------------------
# -- Lists Methods --
# -------------------

# append()
 
myFriends = ["Osama", "Ahmed", "Sayyed"]
myOldFriends = ["Haytham", "Samah", "Ali"]

myFriends.append("Alaa")
myFriends.append(100)
myFriends.append(150.200)
myFriends.append(True)
myFriends.append(myOldFriends)

print(myFriends)
print("=" * 40 )

print(myFriends[2])
print(myFriends[6])
print(myFriends[7])

print("=" * 40 )
print(myFriends[7][2])

print("=" * 40 )
# extend() 

a = [1, 2, 3, 4]
b = ["A", "B", "c"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)

print(a)

print("=" * 40 )
# remove()

x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
print(x)
x.remove("Osama")

print(x)

print("=" * 40 )
# sort()

y = [1, 2, 100, 120, -10, 17, 29]
print(y)

y.sort()
print(y)

y.sort(reverse = True)
print(y)

print("=" * 40 )
# reverse()

z = [10, 1, 9, 80, 100, "Osama", 100]
z.reverse()
print(z) 