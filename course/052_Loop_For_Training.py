# -----------------
# -- Loop => For --
# --  Trainings  --
# -----------------

print("=" * 40)
# Range :
print("# Range :")

# myRange = range(1, 101)

# for number in myRange :
#     print(number)

print("=" * 40)
# mySkills :
print("# mySkills :")

mySkills = {
    "Html": "90%",
    "Css": "60%",
    "PHP": "70%",
    "JS": "80%",
    "Python": "90%",
    "MYSQL": "60%"
}

# print(mySkills["JS"])
# print(mySkills.get("Python"))

for skill in mySkills :
    print(f"My Progress in lang {skill} is: {mySkills.get(skill)}")