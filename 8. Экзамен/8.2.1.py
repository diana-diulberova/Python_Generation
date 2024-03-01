n = int(input())
total = 0
while n != 0:
    a = n % 10
    if a % 2 == 0:
        total += a
    n //= 10
print(total)
