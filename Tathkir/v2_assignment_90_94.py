print("=" * 40)
# assignment 1: 
print("# assignment 1:")


# NUM = input("Add Your Number : ")

# if len(NUM) > 1 :
#     raise IndexError (": Only One Character Allowed")

# elif NUM.isalpha() :
#     raise Exception (": Only Numbers Allowed")

# elif 0 < int(NUM) <10 :
#     print(f"The Number Is {NUM}")

# elif int(NUM) == 0 :
#     raise ValueError (": Number Must Be Larger Than 0")

print("=" * 40)
# assignment 2: 
print("# assignment 2:")

try :
    LETTER = input("Add Letter From A to Z : ")
    
    if LETTER.isalpha() and len(LETTER) == 1 and "A" <= LETTER <= "Z" :
        print(f"You Typed {LETTER}")
    
    elif len(LETTER) != 1 :
        raise IndexError ("The letter len is large than 1")
    
    elif LETTER.isalpha() == False  :
        raise ValueError ("The letter is not upper alpha")
    
    elif not ("A" <= LETTER <= "Z") :
        raise NameError ("The letter is not upper")
    

except ValueError :
    print("The letter Not in A - Z")

except IndexError :
    print("You Must Write One Character Only")

except NameError :
    print("The letter Not uppper")