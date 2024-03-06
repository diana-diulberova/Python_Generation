s = input()

max = 0
b = ''

for i in range(len(s)):
    if s.count(s[i]) >= max:
        max = s.count(s[i])
        b = s[i]
print(b)
