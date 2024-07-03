# объявление функции
def is_magic(date):
    a = int(date[0:2])
    b = int(date[3:5])
    c = int(date[8:10])

    if a * b == c:
        return True
    else:
        return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
