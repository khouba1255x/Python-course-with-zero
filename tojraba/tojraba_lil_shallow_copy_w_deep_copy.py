original_list = [1, 2, [3, 4]]
shallow_copy = list(original_list)
shallow_copy[2][0] = 100

print(original_list)  # Output: [1, 2, [100, 4]]
print(shallow_copy)

print("=" * 40)

import copy

original_list = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original_list)
deep_copy[2][0] = 100

print(original_list)  # Output: [1, 2, [3, 4]]
print(deep_copy)