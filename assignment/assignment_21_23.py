# 1
print("assignment 1")

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends1 = friends.copy()

print(friends[0] + "Method One")
print(friends.pop(0) + "Method Two")  # walli shouf chniyya il method 2

print(friends[0] + " Method One")
print(friends.pop(0) + " Method Two")  # walli shouf chniyya il method 2

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

# 5
print("assignment 5")

friends = ["Osama", "Ahmed", "Sayed"]

friends.insert(0, "Nasser")
friends.insert(4, "Salem")
print(friends)

# 6
print("assignment 6")

friends.pop(1)
friends.pop(2)
print(friends)

friends.pop(-1)
print(friends)

# 7
print("assignment 7")

friends = ['Nasser', 'Ahmed']
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)

print(friends)

# 8
print("assignment 8")

friends.sort()
print(friends)

friends.sort(reverse=True)
print(friends)

# 9
print("assignment 9")

print(len(friends))

# 10
print("assignment 10")

technologies = ["Html", "CSS", "JS", ["Django", "Flask", "Web"]]

print(technologies[3][0])
print(technologies[3][-1])
