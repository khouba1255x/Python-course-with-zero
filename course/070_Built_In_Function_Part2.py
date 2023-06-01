# ------------------------
# -- Built In Functions --
# ------------------------
# sum()
# round()
# range()
# print()
# ------------------------

print("=" * 40)
# sum(iterable, start)

a = [1, 10, 19, 40]

print(sum(a))
print(sum(a, 40))

print("=" * 40)
# round(number, numofdigits)

print(round(150.501))
print(round(150.65, 2))

print("=" * 40)
# range(start, end, step)

print(list(range(0)))
print(list(range(10)))
print(list(range(0, 20, 2)))

print("=" * 40)
# print()

print("Hello Osama How Are You")
print("Hello","Osama","How","Are","You", sep=" @ ")

print("=" * 10)

print("First Line", end="Look Its Me End ")
print("Second Line")