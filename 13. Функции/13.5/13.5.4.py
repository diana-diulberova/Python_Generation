# объявление функции
def is_password_good(password):
    a = 0
    b = 0
    c = 0

    if len(password) >= 8:
        flag = True
    else:
        flag = False
    # print(flag)

    for char in password:
        if flag == True and char in 'ZYXWVUTSRQPONMLKJIHGFEDCBA':
            a += 1

        if flag == True and char in 'abcdefghijklmnopqrstuvwxyz':
            b += 1

        if flag == True and char in '0123456789':
            c += 1


    if a >= 1 and b >= 1 and c >= 1:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
