# Напишите программу, выводящую следующий список:

# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]

# Формат выходных данных

# Программа должна вывести указанный список.

# Примечание 1. Последний элемент списка должен состоять из 26 символов z.

# Примечание 2. Английский алфавит (для копирования) 😇:

# abcdefghijklmnopqrstuvwxyz

str = 'abcdefghijklmnopqrstuvwxyz'
list = []
i = 0

for char in str:
    el = char * (i + 1)
    list.append(el)
    i += 1

print(list)
