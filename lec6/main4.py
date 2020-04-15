my_set = set(['a', 'b', 'c'])
my_set.add('d')
my_set.discard('d')
my_set.discard('hello') # если удалить несуществующий элемент - ничего не будет
my_set.pop() # если удалять из пустого множества - упадет с ошибкой

my_set.clear() # удаляет абсолютно все элементы множества, остается len(my_set) == 0


for i in range(1,11,2): #1,3,5,7,9
    print(i)

for elem in my_set: #'b' ,'a', 'c'
    print(elem)