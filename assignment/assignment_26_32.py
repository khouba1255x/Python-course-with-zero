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