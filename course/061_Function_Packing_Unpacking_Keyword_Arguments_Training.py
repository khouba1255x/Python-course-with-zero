# -----------------------------------------------------
# -- Function Packing, Unpacking Arguments Trainings --
# -----------------------------------------------------

myTuple = ("Html", "CSS", "JS")

mySkills = {
    "Html": "80%",
    "Css": "70%",
    "Python": "50%",
    "MySQL": "80%"
}

def show_skills(name, *skills, **skillsWithProgress) :
    
    print(f"Hello {name} \nskills without Progress is :")
    
    for skill in skills :   
        print(f"- {skill}")
    
    print("Skills With Progress Is : ")
    
    for skill_key, skill_value in skillsWithProgress.items():
        print(f"- {skill_key} => {skill_value}")
    
show_skills("Osama", *myTuple, *mySkills)