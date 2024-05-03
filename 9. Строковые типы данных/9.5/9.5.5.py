str = input()
flag = False

if len(str) == 9 or len(str) == 10:
    for char in str[:1]:
        if char in "АВЕКМНОРСТУХ":
            flag = True
        else:
            flag = False
            break


if flag == True:
    for char in str[1:4]:
        if char in "1234567890":
            flag = True
        else:
            flag = False
            break



if flag == True:
    for char in str[4:6]:
        if char in "АВЕКМНОРСТУХ":
            flag = True
        else:
            flag = False
            break

if flag == True:
    for char in str[6]:
        if char == '_':
            flag = True
        else:
            flag = False
            break

if flag == True:
    for char in str[7:9]:
        if char in "1234567890":
            flag = True
        else:
            flag = False
            break

if flag == True:
    if len(str) == 10:
        for char in str[9]:
            if char.isdigit() == True or char == '':
                flag = True
            else:
                flag = False
                break

if flag == True:
    print('YES')
else:
    print('NO')
