print("=" * 40)
# Assignment 1: 
print("# Assignment 1: ")


# NUM = input("Add Your Number : ")

# if NUM.isalpha() and len(NUM) > 1 :
#     raise IndexError("Only One Character Allowed")

# elif NUM.isdigit() and int(NUM) > 0 :
#     print(f"The Number Is {NUM}")
    
# elif int(NUM) == 0 :
#     raise ValueError("Number Must Be Larger Than 0")

# elif NUM.isalpha() :
#     raise Exception("Only Numbers Allowed")

print("=" * 40)
# Assignemnt 2: 
print("# Assignemnt 2: ")

# LETTER = input("Add Letter From A to Z : ")

# try :
    
#     if len(LETTER) > 1 :
#         raise NameError("You Must Write One Character Only")
    
#     elif 65> ord(LETTER) or ord(LETTER)> 90 :
#         raise NameError("The Letter Not In A - Z")

# except  NameError as e:

#     print(e)


# else :
#     print(f"You Typed {LETTER}")


print("=" * 40)
# Assignment 3: 
print("# Assignment 3: ")

def calculate(num1, num2) -> int:
    return num1 + num2

print(calculate(20, 30))