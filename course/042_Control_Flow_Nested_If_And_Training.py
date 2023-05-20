# ---------------
# -- Nested If --
# ---------------

uName = "Osama"
isStudent = "yes"
uCountry = "Egypt"
cName = "Python Course"
cPrice = 100

print("=" * 40)
# Osamma elzero : 
print("# Osamma elzero :")

if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":
    if isStudent == "yes" :
        print(f"Hello {uName} Because You Are From {uCountry} And Student")
        print(f"The Course \"{cName}\" Price is: ${cPrice - 90}")

    else :
        print(f"Hello {uName} Because You Are From {uCountry}")
        print(f"The Course \"{cName}\" Price is: ${cPrice - 80}")


elif uCountry == "Kuwait" or uCountry == "Bahrain" or "Tunisia" :
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price is: ${cPrice - 50}")

   
else :
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price is: ${cPrice - 30}")




print("=" * 40)
# My work version : 
print("My work version :")

# if uCountry == "Egypt" or "KSA" or "Qatar":
#     print(f"Hello {uName} Because You Are From {uCountry}")
#     print(f"The Course \"{cName}\" Price is: ${cPrice - 80}")
    
# elif uCountry == "Kuwait" or "Bahrain" or "Tunisia" :
#     print(f"Hello {uName} Because You Are From {uCountry}")
#     print(f"The Course \"{cName}\" Price is: ${cPrice - 50}")
    
# else :
#     print(f"Hello {uName} Because You Are From {uCountry}")
#     print(f"The Course \"{cName}\" Price is: ${cPrice - 30}")