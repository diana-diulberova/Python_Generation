# Игра "Числовая угадайка"

import random

n = random.randint(1, 100)

print('Добро пожаловать в числовую угадайку')

def is_valid(num):
    if 0 <= num <= 100:
        return True
    else:
        return False

k = 0
while True:
    user_num = int(input('Пожалуйста, введите число от 1 до 100: '))

    if is_valid(user_num) == False:
        print('А может быть все-таки введем целое число от 1 до 100?')
    else:
        if user_num == n:
            print('Вы угадали, поздравляем!')
            k += 1
            break
        elif user_num < n:
            k += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
        else:
            k +=1
            print('Ваше число больше загаданного, попробуйте еще разок')

print(f'Вы сделали {k} попыток')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

