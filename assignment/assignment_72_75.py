print("=" * 40)
# assignment 1:
print("# assignment 1:")

def remove_chars (string) :
    
    string1 = string[1:-1]
    
    return string1

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# cleaned_list = map(remove_chars, friends_map)
cleaned_list = map(lambda string : string[1:-1], friends_map)

for name in cleaned_list :
    print(name)

print("=" * 40)
# assignment 2:
print("# assignment 2:")

def get_name (name) :
    
    if name[-1] == "m" :
        return True

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

names = filter(get_name, friends_filter)

for name in names :
    print(name)

print("=" * 40)
# assignment 3:
print("# assignment 3:")

print("=" * 10)
# normal function
print("# normal function")

nums = [2, 4, 6, 2]

def multiplication_sum (num1, num2) :
    s = num1 * num2
    return s

from functools import reduce

m_sum = reduce(multiplication_sum, nums)
print(m_sum)

print("=" * 10)
# lambda function
print("# lambda function")

m_sum2 = reduce(lambda num1, num2 : num1 * num2, nums)
print(m_sum2)

print("=" * 40)
# assignment 4:
print("# assignment 4:")

skills1 = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

skills = reversed(skills1)
for index, skill in enumerate(skills, 50) : 
    # print(skill)
    if isinstance(skill, str)  :
        print(f"{index} - {skill}")