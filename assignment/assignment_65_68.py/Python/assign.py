# 2023/5/30 #

print("=" * 40)
# Assignment 1 :
print("# Assignment 1 :")

# Change The cwd 
import os
print(os.getcwd())
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

# Make a 50 file with name f"Text{i}"
for i in range (50) :
    
    # The file nb 25
    if i +1 == 25 :
        file_name = "special-text"
        file_path = os.getcwd()       
        filei = open(f"{file_path}\\{file_name}", "w")
        filei.close()
        
    
    # Any File
    else:
        file_name = f"Text{i +1}.txt"
        file_path = os.getcwd()
        filei = open(f"{file_path}\\{file_name}", "w")
        filei.write(f"Elzero Web School => {i +1}")
        filei.close()
print("=" *20)
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))

# Number of files in folder Python
folder_path = r"C:\khouba\Elzero\Python\Python-course-with-zero\assignment\assignment_65_68.py\Python"
files = os.listdir(folder_path)
file_count = len(files)

print(f"{file_count}")

print("=" * 40)
# Assignment 2 :
print("# Assignment 2 :")

print(os.getcwd())

file1_write = open(r"C:\khouba\Elzero\Python\Python-course-with-zero\assignment\assignment_65_68.py\Python\Text1.txt", "a")
file1_write.write("\nappended => Elzero Web School" * 50)
file1_write.close()

print("=" * 40)
# Assignment 3 :
print("# Assignment 3 :")

file1_write = open(r"C:\khouba\Elzero\Python\Python-course-with-zero\assignment\assignment_65_68.py\Python\Text1.txt", "r")

# number of lines
lines_list = file1_write.readlines()
lines_count = len(lines_list)
print(f"Number Of Lines Is => {lines_count}")

# number of Words
Words_nb = 0

for item in lines_list :
    words = item.split()
    Words_nb += len(words)

print(f"Number Of Words Is => {Words_nb}")

# number of chars 
chars_nb = 0

for item in lines_list :
    words = item.split()
    
    for word in words :
        chars_nb += len(word)

print(f"Number Of Chars Is => {chars_nb}")

# number of "l"
l_nb = 0

for item in lines_list :
    words = item.split()

    
    for word in words :
        l_nb += word.count("l")

print(f"Number Of 'l' Char Is => {l_nb}")

file1_write.close()

print("=" * 40)
# Assignment 4 :
print("# Assignment 4 :")


for i in range (41,51) :
    
    file_name = r"C:\khouba\Elzero\Python\Python-course-with-zero\assignment\assignment_65_68.py\Python\Text"
    os.remove(f"{file_name}{i}.txt")
