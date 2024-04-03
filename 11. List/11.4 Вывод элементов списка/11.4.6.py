# На вход программе подается натуральное число n, затем n строк, затем
# число k — количество поисковых запросов, затем
# k строк — поисковые запросы. Напишите программу,
# которая выводит все введенные строки,
# в которых встречаются одновременно все поисковые запросы.


n = int(input())
list = []

for i in range(n):
    s = input()
    list.append(s)

k = int(input())
list_k = []

for i in range(k):
    search = input()
    list_k.append(search)


for s in list:
    count = 0
    for search in list_k:
        if search.lower() in s.lower():
            count += 1
    if count >= len(list_k):
        print(s)
