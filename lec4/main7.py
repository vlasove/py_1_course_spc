start = 0
stop = 1000000
sum_of_even = 0

while start <= stop:
    if start % 2 == 0:
        sum_of_even += start 
    start += 1
print("Total 1:", sum_of_even)


sum_of_even = 0
start = 0

while start <= stop:
    sum_of_even += start 
    start += 2
print("Total 2:", sum_of_even)

