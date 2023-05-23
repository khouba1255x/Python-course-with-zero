# -------------------------------------------------
# -- Function Packing, Unpacking Arguments *Args --
# -------------------------------------------------

print("=" * 40)

# print(1, 2, 3, 4)

# myList = [1, 2, 3, 5]

# print(myList)
# print(*myList)

print("=" * 40)

# def say_hello(*peoples) :
        
#     for name in peoples :
#         print(f"Hello {name}")
        
# say_hello("Osama", "Ahmed", "Sayed")

print("=" * 40)

def show_details(name, *skills) : 
    
    print(f"Hello {name} Your skills is : ")
    
    for skill in skills :
        print(skill)

show_details("Osama", "Css", "JS")
show_details("Ahmed", "Html", "Css", "JS", "Python", "PHP")