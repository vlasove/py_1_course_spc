count = 0
num = float(input())
while num % 2 == 0:
    count += 1
    print("MALADEC. Input even numver again")
    num = float(input())

print("You lose. Points:", count)