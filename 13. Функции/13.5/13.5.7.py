# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.

# объявление функции
def is_valid_password(password):
    list = psw.split(':')

    if len(list) != 3:
        return False


    else:
        a = list[0]
        a_1 = a[::-1]
        if a != a_1:
            return False


        else:
            b = int(list[1])
            k = 0
            for i in range(2, b // 2+1):
                if (b % i == 0):
                    k += 1
            if (k <= 0):
                d = 1
            else:
                d = 0

            if d == 0:
                return False


            else:
                c = int(list[2])
                if c % 2 == 0:
                    return True
                else:
                    return False




# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
