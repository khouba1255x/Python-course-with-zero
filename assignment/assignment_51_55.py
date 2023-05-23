print("=" * 40)
# assignment 1:
print("# assignment 1:")

# my_nums = [15, 81, 5, 17, 20, 21, 13]

# division_5 = []

# for index in range (len(my_nums)) :
#     if my_nums[index] % 5 == 0 :
#         division_5.append(my_nums[index])

# division_5.sort(reverse= True)

# for i in range (len(division_5)) :
#     print(f"{i +1} => {division_5[i]}")

# else :
#     print("All Numbers printed")

print("=" * 40)
# assignment 2:
print("# assignment 2:")

# for i in range (20) :
    
#     if i == 12 or i == 8 or i == 6 :
#         continue
#     print(str(i).zfill(2))

# else :
#     print("All Numbers Printed")
    
print("=" * 40)
# assignment 3:
print("# assignment 3:")

# my_ranks = {
#     "Math": "A",
#     "Science": "B",
#     "Drawing": "A",
#     "Sports": "C"
# }

# notes = {
#     "A": 100 ,
#     "B": 80,
#     "C": 40
# }

# total = 0

# for subject, note  in my_ranks.items() :
#     print(f"My Rank in {subject} is {note} And This Equal {notes[note]} Points" )
    
#     total += notes[note]

# print(f"Total Points is {total}")

print("=" * 40)
# assignment 4:
print("# assignment 4:")

students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}


for student, student_note, in students.items() :
    
    print("-" * 40)
    print(f"Student Name => {student}".center(40, "-"))
    print("-" * 40)
    total = 0
    
    for note, per in student_note.items() :
        
        if per == "A":
            per = 100
        
        elif per == "B":
            per = 80
        
        elif per == "C":
            per = 40
        
        elif per == "D":
            per = 20
        
        else : 
            print("error")
        
        total += per
        
        print (f"{note} => {per} Points " )
    print(f"Total Points For {student} is {total}")