# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список их кубов.

n = int(input())
list = []

for i in range(n):
    b = int(input())
    c = b ** 3
    list.append(c)

print(list)
