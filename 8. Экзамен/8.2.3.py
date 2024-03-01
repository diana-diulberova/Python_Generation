n = 4
counter = 0
digit = 0

for i in range(1, n + 1):
    j = int(input())
    if j % 2 != 0:
        counter += 1
        if j > digit:
            digit = j

if counter > 0:
    print(counter)
    print(digit)
else:
    print('NO')
