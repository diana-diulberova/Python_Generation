# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.

# На вход программе подается натуральное число n, а затем
# n различных натуральных чисел. Напишите программу,
# которая удаляет наименьшее и наибольшее значение из указанных чисел,
# а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.

# n = int(input())
# list = []
# list_new = []
# list_new_2 = []

# for i in range(n):
#     x = int(input())
#     list.append(x)


# min_num = min(list)
# for num in list:
#     if num == min_num:
#         continue
#     else:
#         list_new.append(num)

# max_num = max(list_new)
# for num in list_new:
#     if num == max_num:
#         continue
#     else:
#         list_new_2.append(num)

# print(*list_new_2, sep='\n')



n = int(input())
list = []

for i in range(n):
    x = int(input())
    list.append(x)


min_num = min(list)
del list[list.index(min(list))]

max_num = max(list)
del list[list.index(max(list))]

print(*list, sep='\n')
