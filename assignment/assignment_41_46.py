print("=" * 40)
# Assignment 1:
print("# Assignment 1:")

# # inputs
# num1 = int(input("Type The first number : ").strip().rstrip())
# operation = input("Type the operation for this arithmetic operation  : ").strip().rstrip()
# num2 = int(input("Type the second number : ").strip().rstrip())

# # coditions
# if operation == "+":
#     print(f"{num1} {operation} {num2} = {num1 + num2}")

# elif operation == "-":
#     print(f"{num1} {operation} {num2} = {num1 - num2} ")

# elif operation == "*":
#     print(f"{num1} {operation} {num2} = {num1 * num2}")

# elif operation == "/":
#     print(f"{num1} {operation} {num2} = {num1 / num2}")

print("=" * 40)
# Assignment 2:
print("# Assignment 2:")

# age = int(input("Type your age : ").strip().rstrip())

# print( "The is Suitable for you " if age > 17 else "The App is not Suitable for you " )

print("=" * 40)
# Assignment 3:
print("# Assignment 3:")

# # input
# age = int(input("Type how old are you : ").strip().rstrip())



# # coditions 

# if 100 >= age >= 10 :
#     convet_age = input("Type convert the age to months (m) or weeks (w) or days(d) or hours(h) or minutes(min) or seconds(s)  ").strip().rstrip().lower()
    
    
#     # calcul

#     month = age * 12
#     week = month * 4
#     day = age * 365
#     hour = day * 24
#     minute = hour * 60
#     second = minute * 60
    
#     if convet_age == "months" or convet_age == "m" :
#         print(f"Your Age in {convet_age} is {month} Months")
        
#     elif convet_age == "weeks" or convet_age == "w" :
#         print(f"Your Age in {convet_age} is {week} Weeks")
        
#     elif convet_age == "days" or convet_age == "d" :
#         print(f"Your Age in {convet_age} is {day} Days")
        
#     elif convet_age == "hours" or convet_age == "h" :
#         print(f"Your Age in {convet_age} is {hour} Hours")

#     elif convet_age == "minutes" or convet_age == "m" :
#         print(f"Your Age in {convet_age} is {minute} Minutes")

#     elif convet_age == "second" or convet_age == "s" :
#         print(f"Your Age in {convet_age} is {second} Seconds")
        
#     else : 
#         print("The conver is False Please reapeat")

# else : 
#     print("Your age is out of range")

print("=" * 40)
# Assignment 4:
print("# Assignment 4:")

# Input
country = input("Type Your country : ").strip().rstrip().capitalize()

# inforamtions
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country in countries : 
    print(f"Your Coutry Eligible For Discount And The Price After Discount is ${price - discount}")

else :
    print(f"Your Country Not Eligible For Discount And The Price Is {price}")