# -----------------------------------
# -- Errors And Exceptions Raising --
# -----------------------------------
# [1] Exceptions Is A Runtime Error Reporting Mechanism
# [2] Exception Gives You The Message To Understand The Problem
# [3] Traceback Gives You The Line To Look For The Code in This Line
# [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
# [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# [6] raise Keyword Used To Raise Your Own Exceptions
# -----------------------------------------------------------------
print("=" * 40)

# x = -10

# if x < 0 :
#     # print(f"The Number {x} Is Less Than Zero")
    
#     raise Exception(f"The Number {x} Is Less Than Zero")

#     print("This Will Not Print Because The Error")
    
# else :
#     print(f"{x} Is Good Number And Ok")

# print("Print Message After If Condition")

print("=" * 40)

y = "Osama"

if type(y) != int :
    
    raise ValueError("Only Numbers Allowed")

print("Print Message After If Condition")