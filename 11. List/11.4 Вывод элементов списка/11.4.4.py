# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая выводит только уникальные строки, в том же порядке,
# в котором они были введены.

n = int(input())
x = input()
list = []
list.append(x)

for i in range(n-1):
    y = input()
    if y not in list:
        list.append(y)

print(*list, sep='\n')
