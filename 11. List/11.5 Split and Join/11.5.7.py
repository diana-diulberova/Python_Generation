s = input()

num = s.split('.')
flag = False

for i in range(len(num)):
    if int(num[i]) >= 0 and int(num[i]) <= 255:
        flag = True
    else:
        flag = False
        break

if flag == True:
    print("ДА")
else:
    print("НЕТ")
