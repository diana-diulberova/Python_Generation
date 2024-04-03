# На вход программе подается натуральное число n, затем n строк,
# затем еще одна строка — поисковый запрос.
# Напишите программу, которая выводит все введенные строки,
# в которых встречается поисковый запрос.

n = int(input())
list = []
list_new = []

for i in range(n):
    s = input()
    list.append(s)

search = input()

for s in list:
    if search.lower() in s.lower():
        list_new.append(s)

print(*list_new, sep='\n')
