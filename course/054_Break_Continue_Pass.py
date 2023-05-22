# ---------------------------
# -- Break, Continue, Pass --
# ---------------------------

print("=" * 40)
# Continue :
print("# Continue :")

myNumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

for number in myNumbers:
    
    if number == 13 :
        continue 
    
    print(number)
    
print("=" * 40)
# Break :
print("# Break :")

for number in myNumbers:
    
    if number == 13 :
        break 
    
    print(number)
    
print("=" * 40)
# Pass :
print("# Pass :")

for number in myNumbers:
    
    if number == 13 :
        pass

    print(number)