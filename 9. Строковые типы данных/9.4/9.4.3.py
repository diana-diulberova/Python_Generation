n = input()
counter = 0

for _ in range(int(n)):
    s = input()
    a = s.count('11')

    if a >= 3:
        counter += 1

print(counter)
