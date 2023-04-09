# 1
print("assignment 1")

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends1 = friends.copy()

print(friends[0] + "Method One")
print(friends.pop(0) + "Method Two")

print(friends[0] + " Method One")
print(friends.pop(0) + " Method Two")

# 2
print("assignment 2")

print(f"{friends1[0]}, {friends1[1]}, {friends1[-1]}")
print(f"{friends1[1]}, {friends1[3]}")

# 3
print("assignment 3")

print(f"{friends1[1]}, {friends1[2]}, {friends1[-2]}")
print(f"{friends1[-2]}, {friends1[-1]}")

# 4
print("assignmet 4")

friends1.pop(-1)
friends1.insert(6, "Elzero")
friends1.pop(-2)
friends1.insert(-1, "Elzero")
print(friends1)
