# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

print("version 1:" .center(50, "#"))

print("=" * 40)
# List Contains Admins :
admins = ["Ahmed", "Osama", "Sameh", "Manel", "Rahma", "Mahmoud"]

# Login : 
name = input("Please Type YOur Name : ").strip().capitalize()

# if Name is in admin :

if name in admins : 
    print(f"Hello {name} Welcome Back")
    
    option = input("Delete or Update Your Name ? : ").strip().capitalize()
    
    if option == "Update" :
        TheNewName = input("Your New Name Please : ").strip().capitalize()
        
        admins.remove(name)
        admins.append(TheNewName)
    print(admins)
else : 
    print("You are not Admin")