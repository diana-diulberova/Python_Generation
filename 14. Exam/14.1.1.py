# объявление функции
def draw_triangle():
    a = 1
    for i in range(0, 8):
        print(((7-i)*' ') + '*' * a)
        a += 2


# n = input()
# основная программа
draw_triangle()  # вызов функции
