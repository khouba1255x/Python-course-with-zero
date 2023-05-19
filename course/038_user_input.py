# ----------------
# -- User Input --
# ----------------

fName = input('what\' is your First name : ')
mName = input('what\' is your Middle name : ')
lName = input('what\' is your Last name : ')

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print(f"Hello {fName} {mName:.1s} {lName} happy to see you")