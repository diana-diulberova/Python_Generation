s = input()
num = s.split()
list = []

for i in range(len(num)):
    a = int(num[i]) ** 3
    list.append(a)

for i in range(len(list)):
    print(list[i], end=' ')
