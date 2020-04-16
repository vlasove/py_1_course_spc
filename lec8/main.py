n = int(input())

numerator = 0
denominator = 1  # 0/1

for i in range(n): # 1,2,3
    x = int(input()) #4
    y = int(input()) #5 

    numerator = numerator * y + x * denominator
    denominator = denominator * y

print(numerator, "/", denominator) 

