# -------------
# -- Numbers --
# -------------

# Integer
print("Integer")

print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-110))

# Float
print("Float")

print(type(1.500))
print(type(100.99))
print(type(-10.99))
print(type(0.99))
print(type(-0.99))

# Complex
print("Comlex")

myComplexNumber = 5+6j

print("Real Part is: {}".format(myComplexNumber.real))
print("Imaginary Part is: {}".format(myComplexNumber.imag))

# [1] You Can Convert From Int To Float or Complex
# [2] You Can Convert From Float To Int or Complex
# [3] You Cannot Convert Complex To Any Type

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(10+9j)
print(int(10+9j))
