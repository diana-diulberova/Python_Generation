# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая создает список из символов всех строк, а затем выводит его.

n = int(input())
list = []

for i in range(n):
    s = input()
    list.extend(s)

print(list)
