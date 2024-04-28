# s = input()
# str = ''

# for c in s:
#     if c in '1234567890':
#         str = str + c

# print(str)


# digits = [el for el in input() if el.isdigit()]
# print(*digits, sep="")


# print(*[i for i in input() if i in "0123456789"], sep = "")

print(*(i for i in input() if i.isdigit()), sep="")
