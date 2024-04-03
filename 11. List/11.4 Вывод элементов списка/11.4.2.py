# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая для каждого введенного числа x выводит значение функции
# f(x)=x**2+2*x+1, каждое на отдельной строке.

n = int(input())
list = []
list_1 = []

for i in range(n):
    x = int(input())
    list_1.append(x)
    d = x**2+2*x+1
    list.append(d)

print(*list_1, sep='\n')
print()
print(*list, sep='\n')
