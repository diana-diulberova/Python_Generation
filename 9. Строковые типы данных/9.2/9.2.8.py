s = input()

if len(s) == 1:
    print(s)
else:
    a= s[:(len(s) + 1)// 2]
    b = s[(-len(s) + 1) // 2:]
    print(b, a, sep='')
