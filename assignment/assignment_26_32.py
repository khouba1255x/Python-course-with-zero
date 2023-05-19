print("=" * 40)
# 1:
print("assignment 1:")

my_list = [1, 2, 3, 3, 4, 5, 1]

print(type(my_list))
unique_list = list(set(my_list))

print(my_list)
print(unique_list)

unique_list.pop(-1)
print(unique_list)

print("=" * 40)
# 2:
print("assignment 2:")

nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums | letters)
print(nums.union(letters))
nums.update(letters)
print(nums)

print("=" * 40)
# 3:
print("assignment 3:")

my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)
my_set.clear()
print(my_set)

my_set.update(["A", "B"])
print(my_set)

letters.remove("C")
print(letters)

print("=" * 40)
# 4:
print("assignment 4:")

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))

print("=" * 40)
# 5:
print("assignment 5:")

my_skills = {
    "HTML": "90%",
    "CSS": "80%",
    "python":"30%"
}
print(my_skills)

my_skills.update({"AI": "20%"})
print(my_skills)