n = -10 ** 6
counter = 0

for _ in range(8):
    j = int(input())
    if j % 4 == 0:
        counter += 1
        if j > n:
            n = j
if counter > 0:
    print(counter)
    print(n)
else:
    print('NO')
