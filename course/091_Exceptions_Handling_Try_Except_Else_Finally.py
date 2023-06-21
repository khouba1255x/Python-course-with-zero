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
print("=" * 40)

# number = int(input("Write Your Age : "))

# print(number)
# print(type(number))

print("=" * 40)

# try : # Try The Code And Test Errors
    
#     number = int(input("Write Your Age : "))
#     print("Good, This Is Integer From try")

# except : # Handle The Errors If Its Found
    
#     print("Bad, This is Not Integer")

# else : # If Theres No Erros # Momkin fi 7alet mea test7a9hesh 5atir Itha il code s7i7 Hawka taw yatba3lik mil try toul
    
#     print("Good, This Is Integer From else")

# finally : # Run The Code Whatever Happens
#     print("Print From Finally Whatever Happens")


try :
    # print(10 / 0)
    # print(x)
    print(int("Hello"))

except ZeroDivisionError:
    print("Cant Divide")

except NameError:
    print("Identfier Not Found")

except ValueError:
    print("Value Error Elzero")
    
except :
    print("Error Happens")
