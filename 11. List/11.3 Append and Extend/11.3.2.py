# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая создает из указанных строк список и выводит его.


n = int(input())
list_str = []

for i in range(n):
    str = input()
    list_str.append(str)

print(list_str)
