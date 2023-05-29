# --------------------------------
# -- File Handling => Read File --
# --------------------------------

myFile = open(r"C:\Users\Mega-PC\osama.txt", "r")

print("=" * 40)
print(myFile) # File Data Object

print("=" * 10)
print(myFile.name)
print(myFile.mode)
print(myFile.encoding)

print("=" * 40)

# print(myFile.read())
# print("=" * 10)
# print(myFile.read(10))

print("=" * 10)
# print(myFile.readline(5))
# print(myFile.readline())
# print(myFile.readline())

print("=" * 10)
# print(myFile.readlines(25))
# print(type(myFile.readlines()))

print("=" * 10)

for line in myFile :
    
    print(line)
    
    if line.startswith("07") :
        break