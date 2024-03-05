s = input()
count_vowels = 0
count_consonants = 0

for i in range(len(s)):
    if s[i] in 'ауоыиэяюеАУОЫИЭЯЮЁЕ':
        count_vowels += 1
    if s[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        count_consonants += 1
print("Количество гласных букв равно", count_vowels)
print("Количество согласных букв равно", count_consonants)
