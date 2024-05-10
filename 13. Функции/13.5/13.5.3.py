# объявление функции
def is_prime(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
    if num > 1 and flag == True:
        return True
    else:
        return False

def get_next_prime(num):
    x = num + 1
    while is_prime(x) == False:
        x += 1
    else:
        return x

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
