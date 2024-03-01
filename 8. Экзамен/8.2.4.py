n = int(input())

for i in range(0, n):
    if i == 0 or i == n - 1:
        print('*' * 19)
    else:
        print('*', ' ' * 17, '*', sep='')
