count = 0 
while True:
    num = float(input())
    if num % 2 == 0:
        print("MALADEC")
        count += 1
        
    else:
        print("YOU LOSE. POINTS:", count)
        break 

print("AFTER WHILE")
