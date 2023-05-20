# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

print("=" * 40)
# List Contains Admins :
admins = ["Ahmed", "Osama", "Sameh", "Manel", "Rahma", "Mahmoud"]

# Login : 
name = input("Please Type YOur Name : ").strip().capitalize()

# if Name is in admin :

if name in admins : 
    print(f"Hello {name} Welcome Back")
    
    # Update Option 
    option = input("Delete or Update Your Name ? : ").strip().capitalize()
    
    if option == "Update" or option == "U" :
        TheNewName = input("Your New Name Please : ").strip().capitalize()
        admins[admins.index(name)] = TheNewName
        
        print("Name Updated : ")
        print(admins)
    
    # Delete Option 
    elif option == "Delete" or option == "D" :
        admins.remove(name)
        
        print("Name Deleted :")
        print(admins)
    
    # Wrong Option
    else :
        print("Wrong Option Choosed")
        
else : 
    
    status = input("Not Admin, Add You Y or N? : ").strip().capitalize()
    
    if status == "Y" or status == "Yes" :
        admins.append(name)
        
        print("You Have Been Added")
        print(admins)
    
    else :
        print("You are not Added.")