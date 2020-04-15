word1 = input()
while True:
    word2 = input()
    if word1[-1] == word2[0]:
        word1 = word2 
    else:
        print(word2)
        break
