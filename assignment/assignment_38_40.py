print("=" * 40)
# 1:
print("Assignment 1:")

# name = input('What\'s your name : ').strip().capitalize()

# print(f"Hello {name}, Happy to see you here")

print("=" * 40)
# 2:
print("Assignment 2:")

# age = int(input("how old are you : "))


# # mel9ich 7al e5ir ken bil if :
# if age > 16 :
#     print("Hello Your age is {age}, All articles is suibtable for you")
# else : 
#     print("Hello your age is under 16, some articles is not suitable for you")
    
print("=" * 40)
# 3:
print("Assignment 3:")

# first_name = input("Write your first name : ").strip().capitalize()
# second_name = input("Write your second name : ").strip().capitalize()

# print(f"Hello {first_name} {second_name:.1}.")

print("=" * 40)
# 4:
print("Assignment 4:")

email = input("write your email : ").strip()

name = email[:email.index("@")].capitalize()
web = email[email.index("@") +1 : email.index(".")].lower()
domain = email[email.index(".")+1 : ].lower()

print(f"Your name is {name}")
print(f"Email Service provider is {web}")
print(f"Top level Domain is {domain}")