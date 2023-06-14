print("=" * 40)
# Assignment 1:
print("# Assignment 1:")

import datetime

date = datetime.datetime(2021, 6, 25)
dateNow = datetime.datetime.now()

print(f"Days From {date.strftime('%Y - %m - %d')} To {dateNow.date()}  Is => {(dateNow - date).days}")

print("=" * 40)
# assignment 2:
print("# assignment 2:")

dateNow = datetime.datetime(2021, 8, 10)

print(dateNow.strftime("%Y-%m-%d"))
print(dateNow.strftime("%b %d, %Y"))
print(dateNow.strftime("%d / %b / %Y"))
print(dateNow.strftime("%d / %b / %y"))
print(dateNow.strftime("%d / %B / %Y"))
print(dateNow.strftime("%a, %d / %B / %Y"))