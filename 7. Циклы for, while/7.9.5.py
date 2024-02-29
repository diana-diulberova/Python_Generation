n = int(input())

while n // 10 != 0:
    total = 0
    while n > 0:
       a = n % 10
       total += a
       n //= 10
    n = total
print(n)
