# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая сначала выводит все отрицательные числа, затем нули,
# а затем все положительные числа, каждое на отдельной строке.
# Числа должны быть выведены в том же порядке, в котором они были введены.


n = int(input())
list = []

for i in range(n):
    x = int(input())
    list.append(x)

for x in list:
    if x >= 0:
        continue
    else:
        print(x)


for x in list:
    if x != 0:
        continue
    else:
        print(x)


for x in list:
    if x <= 0:
        continue
    else:
        print(x)
