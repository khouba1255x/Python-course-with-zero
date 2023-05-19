# ---------------------------
# -- Practical Slice Email --
# ---------------------------

print("=" * 40)
# My work :
print("# My work :")

# theName = input('what\'s Your name?')
# theEmail = input('What\'s Your Email?')

# theName = theName.strip().capitalize()
# theEmail = theEmail.strip()

# theEmail_username = theEmail.index("@") 
# theEmail_website = theEmail.index(".")

# print(f"Hello {theName} Your Email is {theEmail}")
# print(f"Your Username is {theEmail[:theEmail_username]} and Your Website is {theEmail[theEmail_username +1:theEmail_website]}")

print("=" * 40)
# The zero work :
print("# The zero work :") 

theName = input('what\'s Your name?').strip().capitalize()
theEmail = input('What\'s Your Email?').strip()

theUsername = theEmail[:theEmail.index("@")] 
theWebsite = theEmail[theEmail.index("@") +1:]

print(f"Hello {theName} Your Email is {theEmail}")
print(f"Your Username is {theUsername} \nYour Website is {theWebsite}")





print("=" * 40)

# email = "Osama@elzero.org"
# print(email[0:5])

# print("=" * 40)

# email = "Osama_elzero@elzero.org"
# print(email[:(email.index("@"))])