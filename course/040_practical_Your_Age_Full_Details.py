# -------------------------------------
# -- Practical Your Age Full Details --
# -------------------------------------

print("=" * 40)
# Input Age :
print("# Input Age :")

age = int(input('What\'s Your Age ? ').strip())

# Get Age in All Time Units :
print("# Get Age in All Time Units :")

months = age * 36
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("You Lived For:")
print(f"{months} Months.")
print(f"{weeks:,} Weeks.")
print(f"{days:,} Days.")
print(f"{days:,} Days.")
print(f"{minutes:,} Minutes.")
print(f"{seconds:,} Seconds.")