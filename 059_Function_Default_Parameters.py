# ---------------------------------
# -- Function Default Parameters --
# ---------------------------------

print("=" * 40)

def say_hello(name = "Unknown", age= "unknown", country= "Unknown"):
    
    print(f"Hello {name} Your age is {age} and Your Country is {country}")
    
say_hello("Osama", 36, "Egypt")
say_hello("Mahmoud", 28, "KSA")
say_hello("Sameh", 28)
say_hello("Ramy")
say_hello()
