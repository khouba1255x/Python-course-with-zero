# ------------------------
# -- Built In Functions --
# ------------------------
# enumerate()
# help()
# reversed()
# ------------------------

print("=" * 40)
# enumerate(iterable, start=0)

mySkills = ["Html", "Css", "Js", "PHP"]
mySkillsWithCounter = enumerate(mySkills, 20)

print(type(mySkillsWithCounter))

# for skill in mySkillsWithCounter :
#     print(skill)

print("=" * 10)

for counter, skill in mySkillsWithCounter :
    print(f"{counter} // {skill}")

print("=" * 40)
# help()
print("# help()")

# help(print)

print("=" * 40)
# reversed(iterable)
print("# reversed(iterable)")

myString = "Elzero"
print(reversed(myString))

for letter in reversed(myString) :
    print(letter)