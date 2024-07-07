
# alph = ['АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
# direction = input('Выбери направление: \n(+) - Шифрование \n(-) - Дешифрование:\n ')
# lang = int(input('Выбери язык алфавита: \n0 - Русский \n1 - Английский: \n'))
# step = int(direction + input('Введи число, шаг сдвига (со сдвигом вправо): '))
# text = input('Введите текст для обработки:\n')

# for i in text:
#     if i.isalpha():
#         char = alph[lang][(alph[lang].index(i.upper()) + step) % len(alph[lang])]
#         print(char if i.isupper() else char.lower(), end='')
#     else:
#         print(i, end='')


def encrypt(text: str) -> str:
    words = []

    for word in text.split():
        new_word = ''
        word_len = len([c for c in word if c.isupper() or c.islower()])

        for char in word:
            if char.isupper():
                new_word += chr((ord(char) + word_len - 65) % 26 + 65)
            elif char.islower():
                new_word += chr((ord(char) + word_len - 97) % 26 + 97)
            else:
                new_word += char
        words.append(new_word)

    return ' '.join(words)


text = input()
print(encrypt(text))
