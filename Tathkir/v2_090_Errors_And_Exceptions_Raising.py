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

# # Part 1
# x = -10 

# if x < 0 :
    
#     raise Exception(f"The number {x} Is Less Than Zero")  # tajjem ta3mel il exception bil tari9a hethi 

#     print("This will Not Print Because The Error")

# else :
#     print(f"{x} Is Good Number and Ok")
    
# print("Print Message After If  Condition")

print("=" * 40)

# Part 2

y = "Osama"

if type(y) != int :
    
    raise ValueError ("Only Numbers Allowed")  # tajjem t7aded il naw3 mta3 il exception 

print("Print Message After If Condition")