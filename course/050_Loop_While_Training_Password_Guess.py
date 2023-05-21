# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------

tries = 4
mainPassword = "Osama@123"

inputPassword = input("Write Your Password: ")

while inputPassword != mainPassword :
    
    tries -= 1
    
    print(f"Wrong Password, { 'Last' if tries == 1 else tries } Chance left")
    inputPassword = input("Write Your Password: ")
    
    if tries == 1 :
        print("All Tries is Finished.")
        print("Will Not Correct!")
        break
    
else :
    print("The Correct Password")
    
print("Loop is Done ")
    
    