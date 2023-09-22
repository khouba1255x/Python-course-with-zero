print("=" * 40)
# assignment 1: 
print("# assignment 1: ")

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0])
print(friends.pop(0))

print(friends[-1])
print(friends.pop(-1))

print("=" * 40)
# assignment 2 :
print("# assignment 2 :")

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(f"{friends[1]}, {friends[2]}, {friends[-1]}")
print(f"{friends[2]}, {friends[-2]}")

print("=" * 40)
# assignment 3 :
print("# assignment 3 :")

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(f"{friends[1]}, {friends[2]}, {friends[3]}")
print(f"{friends[3]}, {friends[4]}")

print("=" * 40)
# assignment 4 :
print("# assignment 4 :")

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

friends[3] = "Osama"
friends[4] = "Osama"

print(friends)

print("=" * 40)
# assignment 5 :
print("# assignment 5 :")

friends = ["Osama", "Ahmed", "Sayed"]

friends.insert(0, "Nasser")
friends.append("Salem")

print(friends)

print("=" * 40)
# assignment 6 :
print("# assignment 6 :")

friends.pop(0)
friends.pop(0)
print(friends)

friends.pop(-1)
print(friends)

print("=" * 40)
# assignment 7 :
print("# assignment 7 :")

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)

print(friends)

print("=" * 40)
# assignment 8 :
print("# assignment 8 :")

friends.sort()
print(friends)

friends.sort(reverse=True)
print(friends)

print("=" * 40)
# assignment 9 :
print("# assignment 9 :")

print(len(friends))

print("=" * 40)
# assignment 10 :
print("# assignment 10 :")

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[-1][0])
print(technologies[-1][-1])