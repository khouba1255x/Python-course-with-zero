print("=" * 40)
# Assignment 1:
print("# Assignment 1:")

# Line 1
from random import randint
print(f"Random Number Between 10 and 50 => {randint(10, 50)}")

# Line 2

nb = randint(2, 10)
while True:
    
    if nb %2 == 1 :
        
        nb += 1 
        print(f"Random Even Number Between 2 and 10 => {nb}")
        break
    
    else :
        
        print(f"Random Even Number Between 2 and 10 => {nb}")
        break

# Line 2

nb = randint(1, 9)
while True:
    
    if nb %2 == 1 :
        
        print(f"Random Odd Number Between 1 and 9 => {nb}")
        break
    
    else :
        
        nb += 1 
        print(f"Random Odd Number Between 1 and 9 => {nb}")
        break