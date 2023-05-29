# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

print("=" * 40)
# myFile = open(r"C:\khouba\Elzero\Python\Python-course-with-zero\course\osama.txt", "w")
# myFile.write("Hello\n")
# myFile.write("Second Line")

print("=" * 40)

# myFile = open(r"C:\khouba\Elzero\Python\Python-course-with-zero\course\fun.txt", "w" )
# myFile.write("Elzero Web School\n" * 1000)

print("=" * 40)

# myList = ["Osama\n", "Ahmed\n", "Sayed\n"]

# myFile = open(r"C:\khouba\Elzero\Python\Python-course-with-zero\course\Osama1.txt", "w" )
# myFile.writelines(myList)

print("=" * 40)

myFile = open(r"C:\khouba\Elzero\Python\Python-course-with-zero\course\Osama1.txt", "a" )
myFile.writelines("Elzero")
