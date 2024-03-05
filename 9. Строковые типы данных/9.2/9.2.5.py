s = input()

a = s[::-1]
Flag = False

for i in range(len(s)):
    if s[i] != a[i]:
        Flag = False
        break
    else:
        Flag = True

if Flag == False:
    print("NO")
else:
    print("YES")
