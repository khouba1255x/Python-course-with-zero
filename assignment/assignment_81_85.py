print("=" * 40)
# Assignment 1:
print("# Assignment 1:")

def reverse_string(my_string):
    
    for i in range (1, len(my_string)+1) :
        yield my_string[-(i)]
    
    

for c in reverse_string("rayen"):
    print(c)


print("=" * 40)

def Decorators1(func): 
    
    def add_sugar() :
        
        print("Sugar Added From Decorators")
        func()
        print("#" * 20)
    return add_sugar

@Decorators1
def make_tea() : 
    print("Tea Created")

@Decorators1
def make_coffee() : 
    print("Coffee Created")

make_tea()
make_coffee()