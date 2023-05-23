print("=" * 40)
# Assignment 1:
print("# Assignment 1:")

# #
# def calculate(n1, sign, n2) :
    
#     if sign == "add" or sign == "a" or sign == "+" :
#         total = n1 + n2
    
#     elif sign == "subtract" or sign == "s" or sign == "-" :
#         total = n1 - n2
    
#     elif sign == "multiply" or sign == "m" or sign == "*":
#         total = n1 * n2
    
#     else :
#         total = "None, The Sign don't correct !!"
    
#     return (f"Total is : {total}")
    

# num1 = int(input("Type The First number : "))
# sign_arithmatique = input("Type The sign of this calcul -, +, * : ").strip().rstrip().lower()
# num2 = int(input("Type The Second number : "))

# print(calculate(num1, sign_arithmatique, num2))

print("=" * 40)
# Assignment 2:
print("# Assignment 2:")

def addition(*num) :
    
    total = 0

    if num == 10 :
        total += 0
    
    elif num == 5 :
        total -= 5
    
    else :
        total += num
    
    return total

len_list = int(input("Type lengh of your list addition : "))

for i in range (len_list) :
    
    sum_numbers = 0
    
    number = int(input(f"Type Your number {i+1} to add with the total : {sum_numbers} : "))
    
    sum_numbers += addition(number)

print(f"The total of your list is : {sum_numbers}")