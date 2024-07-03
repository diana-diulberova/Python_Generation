from math import factorial

# объявление функции
def compute_binom(n, k):
    index = factorial(n) // (factorial(k) * (factorial(n - k)))
    return index

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
