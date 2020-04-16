# set() - коллекция, хранящая уникальную группу объектов в неупорядоченной форме. Хранит объекты любого типа.
# str() - коллекция, хранящая индексированные единичные подстроки (символы). Хранит объекты только одного типа (str). Неизменяемая коллекция.
# list() - коллекция, хранящая индексируемую группу объектов. Хранит объекты любого типа. Изменяемая коллекция.
# tuple() - коллекция, хранящая индексируемую группу объектов. Хранит объекты любого типа. Неизменяемая коллекция.

test_set = set()
test_str= str()
test_tuple= tuple()
test_list= list()

for i in range(0,1000):
    test_set.add(i)
    test_str += str(i) 
    test_tuple += (i,)
    test_list.append(i)

print("Test set:", test_set.__sizeof__())
print("Test str:", test_str.__sizeof__())
print("Test list:", test_list.__sizeof__())
print("Test tuple:", test_tuple.__sizeof__())