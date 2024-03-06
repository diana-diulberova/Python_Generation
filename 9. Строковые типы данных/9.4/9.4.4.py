s = input()
counter = 0

for i in range(len(s)):
    if s[i] in "0123456789":
        counter += 1
print(counter)
