# -----------------------------
# -- Tuple --
# -----------
# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item
# [4] Tuple Are Immutable => You Cant Add or Delete
# [5] Tuple Items Is Not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples
# -----------------------------

# Tuple Syntax & Type Test

myAwesomeTubleOne = ("Osama", "Ahmed")
myAwesomeTubleTwo = "Osama", "Ahmed"

print(myAwesomeTubleOne)
print(myAwesomeTubleTwo)

print(type(myAwesomeTubleOne))
print(type(myAwesomeTubleTwo))

print("=" * 40)
# Truple Indexing 

myAwesomeTubleThree = (1, 2, 3, 4, 5)
print(myAwesomeTubleThree[0])
print(myAwesomeTubleThree[-1])
print(myAwesomeTubleThree[-3])

print("=" * 40)
# Tuple Assign Values

myAwesomeTubleFour = (1, 2, 3, 4, 5)

# myAwesomeTubleFour[2] = "Three" # TypeError: 'tuple' object does not support item assignment
# print(myAwesomeTubleFour) 

print("=" * 40)
# Tuples Items 

myAwesomeTubleFive = ("Osama", "Osama", 1, 2, 3, 100.5, True)
print(myAwesomeTubleFive[1])
print(myAwesomeTubleFive[-1])