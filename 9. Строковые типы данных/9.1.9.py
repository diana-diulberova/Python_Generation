s = input()
a = s[0]
count = 0

for i in range(1, len(s)):
    if s[i] == a:
        count += 1
    a = s[i]
print(count)
