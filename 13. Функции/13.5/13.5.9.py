# объявление функции
def convert_to_python_case(text):
    lst = list(txt)
    # print(lst)
    lst_1 = []
    lst_1.append(lst[0].lower())
    # print(lst_1)

    for el in lst[1:]:
        if el.isupper():
            lst_1.append('_')
            lst_1.append(el.lower())
        else:
            lst_1.append(el)

    text = ''.join(lst_1)

    return text


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
