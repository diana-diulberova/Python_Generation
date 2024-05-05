# объявление функции
def print_digit_sum(num):
    list = [int(i) for i in str(num)]
    # print(list)
    num = sum(list)
    print(num)


# считываем данные
n = input()

# вызываем функцию
print_digit_sum(n)
