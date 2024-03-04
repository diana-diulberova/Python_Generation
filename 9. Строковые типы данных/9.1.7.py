s = input()
Flag = "Цифр нет"

for i in range(len(s)):
        if s[i] in "0123456789":
            Flag = "Цифра"
            break


print(Flag)
