print("=" * 40)
# assignment 1:
print("# assignment 1:")

# num = int(input("Type a number > 0 : ").strip().rstrip())

# if num > 0 :
    
#     i = num
#     while i > 0 : 
        
#         if i == 6 or i == num :
#             i -= 1
        
#         else :
#             print(i)
#             i -= 1
        
#     if num > 5 :
#         print(f"The output is Complet, {num -2} Numbers printed Successfully.")

#     else :
#         print(f"The output is Complet, {num -1} Numbers printed Successfully.")
            
# else : print("The number is less then 0, type more than")

print("=" * 40)
# assignment 2:
print("# assignment 2:")

# # friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

# friends_number = int(input("Type How many much have friends : "))

# friends = []
# i = 0
# while True :
#     if i < friends_number :
#         friends.append(input(f"Type name your friend {i +1} : ").strip().rstrip())
#         i += 1
#     else : 
#         break
    
# print(friends)
# i = 0
# skip = 0

# while i < friends_number :
    
#     if friends[i] == friends[i].capitalize() :
#         print(friends[i])
#     else :
#         skip += 1
#     i += 1
    
# print(f"Friends Printed And Ignored Name Comunt is {skip}")

print("=" * 40)
# assignment 3:
print("# assignment 3:")
# # 1:

# skills = ["HTML", "CSS", "JavaScipt", "PHP", "Python"]

# while skills :
#     print(skills)
#     break

print("=" * 10)
# # 2:

# i = 0
# while len(skills)>i :
#     print(skills[i])
#     i += 1

print("=" * 10)
# #3: hetheya houwa il s7i7 7asb il condition elli 3tahomly , 5demt bi chatgbt

# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

# while skills:
#     print(skills.pop(0))

print("=" * 40)
# assignment 4:
print("# assignment 4:")

my_friends = []

maxi = 1
maxi_list = 4
while maxi < 5 :
    name = input(f"Type Name Your Friend number {maxi} : ").strip().rstrip()
    
    if name == name.upper() :
        print("The Name Is Invalid !!")
    
    elif name == name.capitalize() :
        print(f"Friend {name} Added")
        my_friends.append(name)

        
        maxi += 1
        maxi_list -=1
        print(f"Names Left in List Is {maxi_list}")
        
        
    else :  
        print("The Name Is Valid")
        my_friends.append(name.capitalize())
        
        print(f"Friend {name} Added => 1st Letter Become Capital") 
               
        maxi += 1
        maxi_list -=1
        print(f"Names Left in List Is {maxi_list}")
        
print(my_friends)