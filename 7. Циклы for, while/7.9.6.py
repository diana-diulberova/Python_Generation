import math
n = int(input())
total = 0

for i in range(1, n+1):
    a = math.factorial(i)
    total += a

print(total)
