# объявление функции
def find_all(target, symbol):
    list = []
    target = [c for c in target]
    print(target)
    for i in range(len(target)):
        if target[i] == symbol:
            list.append(i)
    return list

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
# print(find_all('abcdabcaaa', 'a'))
# print(find_all('abcadbcaaa', 'e'))
# print(find_all('abcadbcaaa', 'd'))
