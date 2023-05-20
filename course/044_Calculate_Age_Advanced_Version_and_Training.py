# -------------------------------------------------
# -- Calculate Age Advanced Version and Training --
# -------------------------------------------------

# Write Note :

print("#" * 80)
print(" You Can write The First Letter Or Full Name of The time Unit ".center(80, "#"))
print("#" * 80)

print("=" * 40)
# Collet Age Data :
print("# Collet Age Data :")

age = input("Please Write Your Age : ").strip()

# Collect Time Unit Data :
unit = input("Please Choose Time Unit: Months, Weeks, Days : ").strip().lower()

# Get Time Units : 

months = int(age) * 12
weeks = months * 4
days = int(age) * 365

if unit == "months" or unit == "m" : 
    print("You Choosed The Unit Months")
    print(f"You Lived For {months:,} Months")
    
elif unit == "weeks" or unit == "w" : 
    print("You Choosed The Unit Weeks")
    print(f"You Lived For {weeks:,} Weeks")
    
elif unit == "days" or unit == "d" : 
    print("You Choosed The Unit Days")
    print(f"You Lived For {days:,} Days")
    
else : 
    print("error")