# --------------------
# -- Function Scope --
# --------------------

# x = 1  # Global Scope

def one():
        
    x = 2
    global x
    
    print(f"Print Variable From Function Scope {x}")
    


def two():
    
    x = 10
    print(f"Print Variable From Function Scope {x}")


one()
print(f"Print Variable From Global Scope {x}")
two()
print(f"Print Variable From Global Scope After One Function Is Called : {x}")