# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------
print("=" * 40)

country = "Egypt"

if country == "Egypt" : print(f"The Weather in {country} is 15")

elif country == "KSA" : print(f"The Weather in {country} is 30")

else : print("Country is not in the list")

print("=" * 40)
# Short if :
print("# Short if :")

movieRate = 18
age = 18

if age < movieRate :
    print("Movie is Not Good 4u") # Condition if True
    
else : 
    print("Movie is Good 4u and Happy Watching") # Condition if False
    

print("Movie is Not Good 4u" if age < movieRate else "Movie is Good 4u and Happy Watching")

# Condition if True | If Condition | Else | Condition if False :
