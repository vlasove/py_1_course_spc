number = int(input())



item = -number 
while item < number + 1:
    print(item, "and", item ** 2)
    item += 1

for item in range(-number, number + 1, 1):
    print(item, "and", item ** 2)