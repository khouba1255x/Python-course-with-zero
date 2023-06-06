# 73

# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True
# [5] The Function Need To Return Boolean Value
# ---------------------------------------------------------------

print("=" * 40)
# Example 1
print("# Example 1")

def checkNumber(num):
    
    return num > 10

myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]

myResult = filter(checkNumber, myNumbers)

for number in myResult :
    print(number)

print("=" * 40)
# Example 2
print("# Example 2")

def checkName(name):
    
    return name.startswith("O")

myTexts = ["Osama", "Omer", "Ahmed", "Sayed", "Othman"]
myReturnedData = filter(checkName, myTexts)

for person in myReturnedData :
    print(person)

print("=" * 40)
# Exemple 3
print("# Exemple 3")

myNames = ["Osama", "Omer", "Ahmed", "Sayed", "Othman", "Ameer"]
myReturnedName = filter(lambda name: name.startswith("A"), myNames)

for p in myReturnedName :
    print(p)