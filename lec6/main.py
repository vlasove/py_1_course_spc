# Коллекции
# Коллекция 1: множество set()

# Множество set() - коллекция, хранящая уникальную группу объектов в неупорядоченной форме.
test_set = set(["Bob", "Alex", "Bob", "Alex", "Victor", "Evgen", "Evgen", "Evgen"])
print(test_set)
name = "Fred"

if name in test_set:
    print("Fred in test_set")
else:
    test_set.add(name)
    test_set.add('Bob')
    print('Fred not in test_set. Adding')
    print(test_set)