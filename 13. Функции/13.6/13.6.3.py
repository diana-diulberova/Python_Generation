import math

# объявление функции
def solve(a, b, c):
    d = b * b - 4 * a * c

    if d > 0:
        x1 = (-1 * b - math.sqrt(d)) / (2 * a)
        x2 = (-1 * b + math.sqrt(d)) / (2 * a)
        return (min(x1, x2)), (max(x1, x2))
    elif d == 0:
        x = (-1 * b) / (2 * a)
        return x, x
    else:
        return "Нет корней"

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
