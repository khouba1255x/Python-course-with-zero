# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors
# Except  => Handle The Errors
# ----------------------------
# Else    => If No Errors
# Finally => Run The Code
# ------------------------

# # part 1 

# number = int(input("Write Your Age: "))

# print(number)
# print(type(number))

# # part 2

# try : # Try The Code And Test Errors
#     number = int(input("Write Your Age: "))
#     print("Good, This Is Iteger From Try")

# except : # Handle The Errors If Its Found
#     print("Bad, This is Not Interger")

# else : # If Theres No Errors
#     print("Good, This Is Iteger From Else")

# finally : 
#     print("Print From Finally Whaterver Happens")

# part 3

try : 
    # print(10 / 0)
    # print(x)
    print(int("Hello"))

except ZeroDivisionError: 
    print("Cant Divide")

except NameError:
    print("The name is not found")

except :
    print("Errors Happens")