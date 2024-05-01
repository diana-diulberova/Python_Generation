s = [int(i) for i in input().split()]
a = 0
print(*s, sep='+', end='=')

for i in range(len(s)):
    a += s[i]
print(a)
