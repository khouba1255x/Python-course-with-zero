# --------------------------------------------
# -- Doc String & Commenting vs Documenting --
# --------------------------------------------
# [1] Documentation String For Class, Module or Function
# [2] Can Be Accessed From The Help and Doc Attributes
# [3] Made For Understanding The Functionality of The Complex Code
# [4] Theres One Line and Multiple Line Doc Strings
# -------------------------------------------------

def elzero_function(name) :
    
    # '''This Is Function To Say Hell From Elzero''' # function document # signle line doc string
    
    """
    Elzero Function
        It Say Hello From Elzero
        prameter : 
            name => Person Name That Use Function
            Return :
                Return Hello Message To The Person
    """
    print(f"Hello {name} From Elzero")

elzero_function("Ahmed")

print(dir(elzero_function)) # for know more attributs about this function 
print(elzero_function.__doc__) # for print the doc

print("=" * 40)

help(elzero_function) # or print the doc with help function 