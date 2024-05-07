def get_factors(num):
    list = [i for i in range(1, num + 1) if num % i == 0]
    return len(list)

# считываем данные
n = int(input())


# вызываем функцию
print(get_factors(n))
