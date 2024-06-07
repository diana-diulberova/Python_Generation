# объявление функции
def is_palindrome(text_2):
    text_3 = text_2[::-1]
    # print(text_3)


    if text_2 != text_3:
        return False

    else:
        return True


# считываем данные
txt = input()
text_1 = txt.lower()
text_2 = ''
text_2 = text_2.join(i for i in text_1 if i.isalpha())
# print(text_2)

# вызываем функцию
print(is_palindrome(text_2))
