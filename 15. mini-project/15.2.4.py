import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

quantity = int(input('Сколько паролей нужно сгенерировать? '))
len_pass = int(input('Сколько символов должно быть в пароле? '))
dig = input('Напишите "да", если в пароле нужны цифры, "нет" - если не нужны. ')
low_let = input('Напишите "да", если в пароле нужны строчные буквы, "нет" - если не нужны. ')
up_let = input('Напишите "да", если в пароле нужны прописные буквы, "нет" - если не нужны. ')
char_yes = input('Напишите "да", если в пароле нужны символы !#$%&*+-=?@^_?, "нет" - если не нужны. ')
char_no = input('Напишите "да", если в пароле нужны неоднозначные символы il1Lo0O, "нет" - если не нужны. ')

if dig == 'да'.lower():
    chars += digits
if low_let == 'да'.lower():
    chars += lowercase_letters
if up_let == 'да'.lower():
    chars += uppercase_letters
if char_yes == 'да'.lower():
    chars += punctuation
if char_no == 'да'.lower():
    chars += 'il1Lo0O'

def generate_password(length, chars):
    for _ in range(quantity):
        password = ''.join(random.choice(chars) for _ in range(length))
        print(password)

generate_password(len_pass, chars)
