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

# Dictionary
print("Dictionary  :  ")

user = {
    "name": "Osama",
    "age": 36,
    "contry": "Egypt",
    "skills": ["Html", "Css", "JS"],
    "rating": 10.5
}

print(user)
print(user["contry"])
print(user.get("contry"))

print(user.keys())
print(user.values())

# Two-Dimensional Dictionary
print("Two-Dimensional Dictionary  :")

languages = {
    "One": {
        "name": "Html",
        "progresse": "80%"
    },
    "Two": {
        "name": "Css",
        "progresse": "90%"
    },
    "Three": {
        "name": "Js",
        "progresse": "90%"
    }
}

print(languages)
print(languages["One"])
print(languages["One"]["progresse"])
