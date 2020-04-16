words = []
n = int(input())

for i in range(n):
    word = input()
    words.append(word)

user_id = int(input()) - 1 

answer = ""

for w in words:
    answer = answer + w[user_id]

print(answer)