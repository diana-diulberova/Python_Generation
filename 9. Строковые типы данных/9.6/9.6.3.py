n = int(input())
s = input()

for c in s:
    a = ord(c) - n

    if a < 97:
        a = 122 - (96 - a)
    print(chr(a), end='')
