s1 = input()
# s1 = s.split()
s2 = s1[1:]
s3 = int(s2)
list = []
list_new = []

# print(s2)

for i in range(s3):
    s4 = input()
    list.append(s4)

# print(list)

for i in range(len(list)):
    if '#' in list[i]:
        a = list[i].index('#')
        # print(a)
        b = list[i][:a]
        # print(b)
        c = b.rstrip()
        list_new.append(c)
    else:
        list_new.append(list[i])

print(*list_new, sep='\n')
