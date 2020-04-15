a_set = set() # множество автобусов по пути туда
b_set = set() # множество автобусов по пути обратно

while True:
    word = input()
    if word == "":
        break
    a_set.add(word)

while True:
    word = input()
    if word == "":
        break
    b_set.add(word)

print(len(a_set.intersection(b_set)))