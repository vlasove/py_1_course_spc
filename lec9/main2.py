# Список list()
# Так же как и set() может хранить в себе объекты разного типа
# Так же как и str() индексируется и возможна операция среза

primes = [2, 3, 5, 7, 11]
print(primes)
print(type(primes))

empt1 = []
empt2 = list()

print(empt1, empt2)
print(len(primes))

sample = [2, 3] * 4
print(sample)

temp = [0] * 10
print(temp)