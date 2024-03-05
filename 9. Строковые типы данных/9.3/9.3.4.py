s = input()

a = s.upper()
counter = 0

for i in range(len(s)):
    if s[i] != a[i]:
        counter += 1

print(counter)
