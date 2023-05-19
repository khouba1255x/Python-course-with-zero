print("=" * 40)
# 1:
print("assignment 1:")

print(bool(100))
print(bool(100.2))
print(bool("srr"))
print(bool(True))

print("=" * 10)

print(bool())
print(bool(""))
print(bool(0))
print(bool(False))

print("=" * 40)
# 2:
print("assignment 2:")

html = 80 
css = 60
javascript = 70

print(html > 50 and css > 50 and javascript > 50)
print(html and css and javascript > 50)

print("=" * 40)
# 3:
print("assignment 3:")

num_one = 10
num_two = 20
num = 20

print(num > num_one or num > num_two)
print(num > num_two and num_one)

print("=" * 40)
# 4:
print("assignment 4:")

num_one = 10
num_two = 20
result = num_one + num_two

print(result)
print(result**3)

result1 = result**3 % 26000
print(result1)

result2 = result1 / 5
print(result2)

result3 = str(result2)
print(type(result3))