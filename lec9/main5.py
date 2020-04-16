primes = [2,3,5,7,11,13]

for i in primes:
    print(i, i**2)

for j in range(len(primes) - 1, -1, -1): #0, 1, 2, 3, 4, 5 range(start=0, stop, step=1)
    print("Id:", j, "elem:", primes[j])

for i in range(len(primes)):
    print(i)