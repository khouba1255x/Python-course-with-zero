# ------------------------
# -- Dictionary Methods --
# ------------------------

# setdefault()
print("# setdefault()   :")

user = {
    "name": "Osama"
}
print(user)
print(user.setdefault("name", "Ahmed"))
print(user.setdefault("age", 36))
print(user.setdefault("Contry"))
print(user)

print("=" * 50)

# popitem()
print("# popitem()  :")

member = {
    "name": "Osama",
    "skill": "PS4"
}
print(member)
member.update({"age": 36})
print(member)
print(member.popitem())
print(member)

print("=" * 50)

# itmes()
print("# itmes()  :")

view = {
    "name": "Osama",
    "skill": "XBox"
}

allItems = view.items()
print(view)
view["age"] = 36
print(view)
print(allItems)

print("=" * 50)

# fromkeys
print("# fromkeys   :")

a = ("MyKeyOne", "MyKeyTwo", "MyKeyThree")
b = "X", "k"
print(dict.fromkeys(a, b))

print("=" * 50)
