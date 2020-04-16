primes = [2, 3, 5, 7, 11]

print("Сумма первых двух простых чисел:", primes[0] + primes[1])
print("Последнее из простых чисел:", primes[-1])

a_set = set()
a_set.add(2)

primes.append(13)
print(primes)
primes.pop()
print("After pop():", primes)

del primes[1]
print("After del:", primes)

a = [1,2,3]
b = [4,5,6]

c = a + b 
print(c)

for item in primes:
    print(item)

if 5 in primes:
    print("YES")



primes[0] = 17
print(primes)