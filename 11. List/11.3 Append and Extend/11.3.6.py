# На вход программе подается натуральное число n, где n ≥ 2
# Затем поступают n целых чисел.
# Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел.

n, a = int(input()), int(input())
list = []

for _ in range(n-1):
    b = int(input())
    list.append(a + b)
    a = b

print(list)