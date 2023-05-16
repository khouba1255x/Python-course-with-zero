# ------------------------
# -- Dictionary Methods --
# ------------------------

print("=" * 40)
# clear() : 
print("# clear() : ")

user = {
    "name": "Osama"
}

print(user)
user.clear()
print(user)

print("=" * 40)
# update() : 
print("# update() : ")

member = {
    "name": "Osama"
}

print(member)
member["age"] = 36
print(member)
member.update({"contry": "Egypt"})
print(member)

print("=" * 40)
# copy() :
print("# copy() :")

main = {
    "name": "Osama"
}

b = main.copy()
print(b)

print("=" * 10)
main.update({"Skills": "fighting"})
print(main)
print(b)

print("=" * 40)
# keys() + values() :  
print("# keys() + values() :  ")

print(main.keys())
print(main.values())