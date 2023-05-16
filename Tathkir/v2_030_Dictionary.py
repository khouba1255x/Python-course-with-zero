# ---------------------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------

print("=" * 40)
# Dictionary :
print("# Dictionary :")

user = {
    "name" : "Osama",
    "age" : 36,
    "country" : "Egypt" ,
    "Skills" : ["Html", "Css", "Js"], 
    "rating" : 10.5 , 
}

print(user)

print("=" * 10)
print(user["country"])
print(user.get("country"))

print("=" * 10)
print(user.keys())
print(user.values())

print("=" * 40)
# Two-Dimensional Dictionary :
print("# Two-Dimensional Dictionary :")

languages = {
    "One" :{
        "name" : "Html" , 
        "progress" : "80%"
    },
    "Two" : {
        "name": "Css",
        "progress": "90%"
    },
    "Three" : {
        "name": "Js",
        "progress": "90%"
    }
}

print(languages)

print("=" * 10)
print(languages["One"])
print(languages["Three"]["progress"])

print("=" * 10)
print(len(languages))
print(len(languages["Two"]))

print("=" * 40)
# Create Dictionary From Variables : 
print("# Create Dictionary From Variables : ")

frameWorkOne = {
    "name": "Vuejs",
    "progress": "80%"
}

frameWorkTwo = {
    "name": "ReactJs",
    "progress": "80%"
}

frameWorkThree = {
    "name": "Angular",
    "progress": "80%"
}

allFramework = {
    "One": frameWorkOne,
    "Two": frameWorkTwo,
    "Three": frameWorkThree
}

print(allFramework)