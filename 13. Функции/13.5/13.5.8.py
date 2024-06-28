# объявление функции
def is_correct_bracket(text):
    lst = list(txt)

    for el in lst:
        if el[0] == '(':
            k = 1
            l = 0
        else:
            return False

        for el in lst[1:]:
            if el == '(':
                k += 1
            elif el == ')':
                l += 1
                if l > k:
                    return False

        if k == l:
            return True
        else:
            return False



# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
