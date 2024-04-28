
# print(*[i ** 2 for i in map(int, input().split()) if not i % 2 and i ** 2 % 10 != 4])
print(*[int(el) ** 2 for el in input().split() if int(el) % 2 == 0 and int(el) ** 2 % 10 != 4])
