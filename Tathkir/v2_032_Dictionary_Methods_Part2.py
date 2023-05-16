# ------------------------
# -- Dictionary Methods --
# ------------------------

print("=" * 40)
# setdefault() : 
print("# setdefault() : ")

user = {
    "name": "Osama"
}

print(user)
print(user.setdefault("name", "Ahmed"))
print(user.setdefault("age"))
print(user.setdefault("age" , 36))
print(user)

print("="  * 40)
# popitem () :
print("# popitem () :")

member = {
    "name": "Osama",
    "skill": "PS4"
}

print(member)
member.update({"age": 36})

print("=" * 10)
print(member)
print(member.popitem()) # popitem fil version 3.7 w ett meshy , walla yrajja3 e5ir , ama 9bal ken ya3mel randim pop
print(member)

print("=" * 40)
# items() : 
print("# items() : ")

view = {
    "name": "Osama",
    "skill": "XBox"
}

allItems = view.items() # deep copy
print(view)

print("=" * 10)
view["age"] = 36

print(allItems)
print(view)

print("=" * 40)
#fromkeys() : 
print("#fromkeys() : ")

a = ("MyKeyOne", "MyKeyTwo", "MyKeyThree")
b = "X"
c = "c"

print(dict.fromkeys(a, b+c)) 