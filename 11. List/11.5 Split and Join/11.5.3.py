s = input()
words = s.split()

for i in range(len(words)):
    print(words[i][0], end='.')
