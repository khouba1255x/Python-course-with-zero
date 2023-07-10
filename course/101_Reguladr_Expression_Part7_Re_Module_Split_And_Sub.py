# ----------------------------------------------------
# -- Regular Expressions => Re Module Split And Sub --
# ----------------------------------------------------
# split(Pattern, String, MaxSplit)  => Return A List Of Elements Splitted On Each Match
# sub(Pattern, Replace, String, ReplaceCount) => Replace Matches With What You Want
# ---------------------------------------------------------------------
print("=" * 40)

import re

string_one = "I Love Python Programming Language"
search_one = re.split(r"\s", string_one,)
print(search_one)

print("=" * 40)

string_two = "How-To-Write_A_Very-Good-Article"
search_two = re.split("-|_", string_two)
print(search_two)

print("=" * 40)

# Get Words Form URL

for counter, word in enumerate(search_two, 1) :
    
    # # my solution
    # if len(word) > 1 :
    #     print(f"Word Number : {counter} => {word.lower()}")

    # Elzero Solution
    if len(word) == 1 :
        continue
    
    print(f"word Number: {counter} => {word.lower()}")
    
print("=" * 40)

my_string = "I Love Python"
print(re.sub(r"\s", "-", my_string, 1))