print("=" * 40)
# 1 : 
print("assignment 1 :")

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mhmoud"]

print("=" * 10)
print(friends[0],"=> Method One")
print(friends[-5], "=> Method Two")

print("=" * 10)
print(friends[-1], "Mehtod One")
print(friends[4], "Mehtod Two")

print("=" * 40)
# 2 :
print("assignment 2 : ")

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mhmoud"]

print(friends[0::2])
print(friends[1::2])

print("=" * 40)
# 3 :
print("assignmnet 3:")

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mhmoud"]

print(friends[1:4])
print(friends[-2:])

print("=" * 40)
# 4 : 
print("assignment 4:")

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mhmoud"]

friends.pop(-1)
friends.pop(-1)

friends.append("Elzero")
friends .append("Elzero")

print(friends)

print("=" * 40)
# 5 : 
print("assignment 5:")

friends = ["Osama", "Ahmed", "Sayed"]

friends.insert(0,"Nasser")
friends.append("Salem")

print(friends)

print("=" * 40)
# 6 : 
print("assignment 6: ")

friends = ['Nasser', 'Osama', 'Ahmed', 'Sayed', 'Salem']

friends.pop(0)
friends.pop(0)

print(friends)

friends.pop(-1)

print(friends)

print("=" * 40)
# 7 :
print("assignment 7 : ")

friends = ['Ahmed', 'Sayed']
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

print("=" * 10)
# type 1 : 
print("type 1 : ")

print(friends + employees + school)

print("=" * 10)
# type 2 :
print("type 2 : ")

friends.extend(employees + school)
print(friends)

print("=" * 40)
# 8 :
print("assignment 8 : ")

friends = ['Ahmed', 'Sayed', 'Samah', 'Eman', 'Ramy', 'Shady']

friends.sort()
print("A => Z : {}".format(friends))

friends.sort(reverse=True)
print("Z => A : {}".format(friends))

print("=" * 40)
# 9 : 
print("assignment 9 : ")

friends = ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']

print("The number of my friends = {}".format(len(friends)))

print("=" * 40)
# 10 :
print("assignment 10 : ")

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[-1][0])
print(technologies[-1][-1])