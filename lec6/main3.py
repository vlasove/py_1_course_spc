n = int(input())

words_set = set()

for i in range(n):
    word = input()
    words_set.add(word)

new_word = input()

if new_word in words_set:
    print('НЕ ЗАСЧИТАНО')
else:
    print('ЗАСЧИТАНО')