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

# def addition(*nums) :
    
#     total = 0

#     for num in nums :
        
#         if num == 10 :
#             total += 0
        
#         elif num == 5 :
#             total -= 5
        
#         else :
#             total += num
    
#     return total



# len_list = int(input("Type lengh of your list addition : "))
# sum_numbers = 0

# for i in range (len_list) :
    
    
#     number = int(input(f"Type Your number {i+1} to add with the total : {sum_numbers} : "))
    
#     sum_numbers += addition(number)

# print(f"The total of your list is : {sum_numbers}")

print("=" * 40)
# Assignment 3:
print("# Assignment 3:")

# #type 1:

# def shwo_shkills(name, skills) :
    
#     if len(skills) > 0 :
#         print(f"Hello {name} Your Skills Is :")
        
#         for skill in skills :
#             print(f"- {skill}")
    
#     else :
#         return(print(f"Hello {name} You Have No Skills To Show"))
    
# name = input("Type Your Name : ").strip().capitalize()
# skills_number = int(input("Type How many Skill You Have : "))
# skills = []

# for i in range (skills_number) :
    
#     skill = input(f"Type Your skill nomber {i+1} : ").strip().capitalize()
#     skills.append(skill)
    
# shwo_shkills(name, skills)

# # type 2:

# def shwo_shkills(name, *skills) :
    
#     if len(skills) > 0 :
#         print(f"Hello {name} Your Skills Is :")
        
#         for skill in skills :
#             print(f"- {skill}")
    
#     else :
#         return(print(f"Hello {name} You Have No Skills To Show"))
        
# shwo_shkills("Osama")

print("=" * 40)
# Assignment 4:
print("# Assignment 4:")

def say_hello(name = "UnKnown", age = "UnKnown", country = "UnKnown") :
    
    return(f"Hello {name} Your Age Is {age} And You Live {country}")

print(say_hello())