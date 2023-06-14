# -----------------------------------
# -- Date and Time => Introduction --
# -----------------------------------
print("=" * 40)

import datetime

print(dir(datetime))
print(dir(datetime.datetime))

print("=" * 40)
# Print The Current Date And Time
print("# Print The Current Date And Time")

print(datetime.datetime.now())

print("=" * 40)

# Print The Current Year
print("# Print The Current Year")
print(datetime.datetime.now().year)

# Print The Current Month
print("# Print The Current Month")
print(datetime.datetime.now().month)

# Print The Current Day
print("# Print The Current Day")
print(datetime.datetime.now().day)


print("=" * 40)
# Print Start And End Of Date
print("# Print Start And End Of Date")

print(datetime.datetime.min)
print(datetime.datetime.max)

print("=" * 40)

print(dir(datetime.datetime.now()))

# Print The Current Time
print(datetime.datetime.now().time())

# Print The Current hour
print(datetime.datetime.now().time().hour)

# Print The Current minute
print(datetime.datetime.now().time().minute)

# Print The Current second
print(datetime.datetime.now().time().second)

print("=" * 40)

# Print Start And End Of Time
print(datetime.time.min)
print(datetime.time.max)

print("=" * 40)
# Print Specific Date
print(datetime.datetime(1982, 10, 25))
print(datetime.datetime(1982, 10, 25, 10, 45, 55, 150364))

myBirthDay = datetime.datetime(1982, 10, 25)
dateNow = datetime.datetime.now()

print(f"My Birthday is {myBirthDay} and ", end="")
print(f"Date Now Is {dateNow}")
print(f"I Lived For {(dateNow - myBirthDay).days} Days.")