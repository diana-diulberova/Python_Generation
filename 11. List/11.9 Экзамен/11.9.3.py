l_1 = [int(i) for i in input().split()]
l_2 = [int(i) for i in input().split()]
list = []

for i in range(len(l_1)):
    c = l_1[i] + l_2[i]
    list.append(c)

print(*list)
