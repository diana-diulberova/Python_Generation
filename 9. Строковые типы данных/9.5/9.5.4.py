n = int(input())
list = []
for i in range(n):
    s = input()
    list.append(s)

for i in range(len(list)):
    if list[i].isspace() == True or list[i] == '':
        print(str(i+1)+':', "COMMENT SHOULD BE DELETED")
    else:
        print(str(i+1)+':', list[i])
