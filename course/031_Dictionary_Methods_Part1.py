# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear()
print("# clear()   :")

user = {
    "name": "Osama"
}
print(user)
user.clear()
print(user)

print("=" * 50)

# update ()
print("# update ()   :")

memeber = {
    "name": "Osama"
}
print(memeber)
memeber["age"] = 36
print(memeber)
memeber.update({"contry": "Egypt"})
print(memeber)

print("=" * 50)

# copy()
print("# copy()   :")

main = {
    "name": "Osama"
}

b = main.copy()
print(b)
main.update({"skills": "Fighting"})
print(main)
print(b)

print("=" * 50)
