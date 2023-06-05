print("=" * 40)
# assignment 1:
print("# assignment 1:")

values = (0, 1, 2)

if any(values) : 
    
    my_var = 0

my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]) :
    print("Good")

else:
    print("Bad")

# The result is : ...

print("=" * 40)
# assignment 2:
print("# assignment 2:")

v = 40

my_range = list(range(v))

print(my_range)
print(sum(my_range))
print(pow(v, v, v))

print(sum(my_range, v) + pow(v, v, v)) 

print("=" * 40)
# assignment 3:
print("# assignment 3:")

n = 20
l = list(range(n))

print(l)
print(round(sum(l) / n))

if round(sum(l) / n) == max (0, 3, 10, 2, -100, -23, 9):
    print("Good")

print("=" * 40)
# assignment 4:
print("# assignment 4:")

print("=" * 10)
# myall
print("# myall")

def myall(iteribal) :
   
    if len(iteribal) > 0 :
           
        if iteribal[0] :
            iteribal.pop(0)
            myall(iteribal)
        
        else : 
            print("False")
             
    else :
        print("True")

myall([1, 2, 3])
myall([1, 2, 3, []])

print("=" * 10)
# myany
print("# myany")

def myany(iteribal) :

    if len(iteribal) > 0 :
           
        if iteribal[0] == True :
            print("True")
        
        else : 
            iteribal.pop(0)
            myany(iteribal)
             
    else :
        print("False")

myany([0, 1, [], False])
myany([0, [], False])

print("=" * 10)
# mymin
print("# mymin")

def mymin(iteribal) :
    
    min1 = 0
    
    for i in range (len(iteribal)) :
        
        if iteribal[i] < min1 :
            min1 = iteribal[i]
    print(min1)

mymin([10, 100, -20, -100, 50])
mymin((10, 100, -20, -1000, 50))

print("=" * 10)
# mymax
print("# mymax")

def mymax(iteribal) :
    
    max1 = 0
    
    for i in range (len(iteribal)) :
        
        if iteribal[i] > max1 :
            max1 = iteribal[i]
    print(max1)

mymax([10, 100, -20, -100, 50, 700])
mymax((10, 100, -20, -100, 50, 7000))