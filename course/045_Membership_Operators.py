# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------

print("=" * 40)
# String :
print("# String :")

name = "Osama"

print("s" in name)
print("a" in name)
print("A" in name)

print("=" * 40)
# List : 
print("# List : ")

friends = ["Ahmed", "Sayed", "Mahmoud"]
print("Osama" in friends)
print("Sayed" in friends)
print("Sayed" not in friends)

print("=" * 40)
# Using In and Not in With condition : 

countriesOne = ["Egypt", "KSA", "Kuwait", "Bahrain", "Syria"]
countriesOneDiscount = 80

countriesTwo = ["Italy", "USA"]
countriesTwoDiscount = 50

myCountry = "Italy"

if myCountry in countriesOne : 
    print(f"Hello You have A Discount Equal To ${countriesOneDiscount}")
    
elif myCountry in countriesTwo :
    print(f"Hello You have A Discount Equal To ${countriesTwoDiscount}")

else : 
    print("You have no discount")