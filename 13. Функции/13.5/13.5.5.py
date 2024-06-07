# объявление функции
def is_one_away(word1, word2):
    count = 0

    if len(word1) == len(word2):
        flag = True
    else:
        flag = False
    # print(flag)

    for i in range(len(word1)):
        if flag == True and word1[i] != word2[i]:
            count += 1

    if count == 1:
        return True
    else:
        return False



# считываем данные
txt1 = input()
txt2 = input()

# # вызываем функцию
print(is_one_away(txt1, txt2))

# print(is_one_away('bike', 'hike'))
# print(is_one_away('water', 'wafer'))
# print(is_one_away('abcd', 'abpo'))
# print(is_one_away('abcd', 'abcde'))
