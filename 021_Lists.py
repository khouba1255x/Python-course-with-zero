# -----------------------------
# -- Lists --
# -----------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# -----------------------------

myAwesomeList = ["One", "Two", "One", 1, 100.5, True]
print(myAwesomeList)
print(myAwesomeList[-1])
print(myAwesomeList[-3])

print(myAwesomeList[1:4])
print(myAwesomeList[:4])
print(myAwesomeList[1:])

print(myAwesomeList[::1])
print(myAwesomeList[::2])

print(myAwesomeList)
# myAwesomeList[1] = 2
# myAwesomeList[-1] = False
myAwesomeList[:3] = ["A", "B", "C"]
print(myAwesomeList)
