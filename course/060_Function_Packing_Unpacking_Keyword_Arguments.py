# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------

print("=" * 40)
# def show_skills(*skills) :
    
#     print(type(skills))

#     for skill in skills :
#         print(f"{skill}")

# show_skills("Html", "CSS", "JS")

print("=" * 40)

mySkills = {
    "Html": "80%",
    "Css": "70%",
    "Js": "50%",
    "Python": "90%"
}

def show_skills(**skills) :
    
    print(type(skills))

    for skill, value in skills.items() :
        print(f"{skill} => {value}")

show_skills(Html = "80%", CSS = "70%", JS = "50%", python = "90%")

print("=" * 10)
print(mySkills)
show_skills(**mySkills)