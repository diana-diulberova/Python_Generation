s = input()

a = s.title()
Flag = False
# print(a)
# print(s)

for i in range(len(s)):
    if s[i] == a[i]:
        Flag = True
    elif s[i] != a[i]:
        Flag = False
        break
    # print(Flag)

if Flag == True:
    print("YES")
elif Flag == False:
    print("NO")
