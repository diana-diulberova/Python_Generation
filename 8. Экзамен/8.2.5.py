n = int(input())

while not 99 < n < 1000:
    n //= 10
print(n % 10)
