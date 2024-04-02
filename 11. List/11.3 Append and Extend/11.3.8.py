# На вход программе подается натуральное число n и n строк, а затем число
# k. Напишите программу, которая выводит
# k-ую букву из введенных строк на одной строке без пробелов.

n = int(input())
list = []
new_str = ''

for i in range(n):
    s = input()
    list.append(s)

k = int(input())

for el in list:
    if len(el) < k:
        new_str += ''
    elif len(el) >= k:
        f = str(el[k-1])
        new_str += f

print(new_str)
