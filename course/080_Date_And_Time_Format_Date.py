# ----------------------------------
# -- Date and Time => Format Date --
# ----------------------------------
# https://strftime.org/
# ---------------------

import datetime

myBirthDay = datetime.datetime(1982, 10, 25)

print(myBirthDay)
print(myBirthDay.strftime("%a"))
print(myBirthDay.strftime("%A"))
print(myBirthDay.strftime("%b"))
print(myBirthDay.strftime("%B"))
print(myBirthDay.strftime("%w"))

print(myBirthDay.strftime("%d/ %B/ %Y"))