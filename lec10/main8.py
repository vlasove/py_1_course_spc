numbers = [1,10,2,3,1,123,1,13,1,1,13,1,1,2,31,3,13,12,124123,412,1]
counts = {}

for num in numbers:
    if num not in counts:
        counts[num] = 1
    else:
        counts[num] += 1

print(counts)