# ---------------------------------------
# -- Function Parameters And Arguments --
# ---------------------------------------

print("=" * 40)

# a, b, c = "Osama", "Ahmed", "Sayed"

# print(f"Hello {a}")
# print(f"Hello {b}")
# print(f"Hello {c}")

# print("=" * 10)

# # def                         => Function Keyword [Define]
# # say_hello                   => Function Name
# # name                        => Parameter
# # print(f"Hello {name}")      => Task
# # say_hello("Akrem")          => Akrem is The Argument

# def say_hello(name):
    
#     print(f"Hello {name}")


# say_hello("Akrem")
# say_hello(a)
# say_hello(b)
# say_hello(c)

print("=" * 40)

# def addition(n1, n2) :
    
#     print(n1 + n2)

# addition(100, 300)
# addition(-50, 100)

print("=" * 40)

def addition(n1, n2) :
    
    if type(n1) != int or type(n2) != int :
        print("Only Integers Allowed")
    
    else :
        print(n1 + n2)

addition(100, 500)

print("=" * 40)

def full_name(first, midle, last):
    
    print(f"Hello {first.strip().capitalize()} {midle.upper():.1s} {last.capitalize()}")
    
full_name("   osama   ", "mohamed", "Elsayed")