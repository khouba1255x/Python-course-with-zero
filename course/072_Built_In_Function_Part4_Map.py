# -------------------------------
# -- Built In Functions => Map --
# -------------------------------
# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------
print("=" * 40)
# Use Map With Predefined Function
print("# Use Map With Predefined Function")

def formatText(text) :
    
    return f"- {text.strip().capitalize()} -"

myTexts = ["OSama", "AHMED", "  sAYed  "]
myFormateData = map(formatText, myTexts)
print(myFormateData)

print("=" * 10)
# print type 1
for name in myFormateData :
    print(name)

print("=" * 10)

# print type 2
for name in list(map(formatText, myTexts)) :
    print(name)

print("=" * 40)
# Use Map With Lamda Function
print("# Use Map With Lamda Function")

for name in list(map(lambda text: f"- {text.strip().capitalize()} - ", myTexts)) :
    print(name)

myTexts = ["OSama", "AHMED", "  sAYed  "]
myFormateData = map(formatText, myTexts)