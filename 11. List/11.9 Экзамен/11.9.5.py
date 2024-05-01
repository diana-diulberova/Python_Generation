s1 = input()
s = list(s1.split('-'))

for c in s1:
    if c in '1234567890-':
        flag = True

    else:
        flag = False
        break

if flag == True:
    if s[0] == '7':
        s.pop(0)

if flag == True:
        if len(s[0]) == 3 and len(s[1]) == 3 and len(s[2]) == 4:
            print('YES')
        else:
            print('NO')

if flag == False:
     print('NO')
