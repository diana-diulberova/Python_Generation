n = int(input())

counter_3 = 0
counter_last = 0
counter_2 = 0
counter_sum_5 = 0
counter_num_7 = 1
counter_num_0 = 0
m = n % 10
while n != 0:
    if n % 10 == 3:
        counter_3 += 1
    if n % 10 == m:
        counter_last += 1
    if n % 10 % 2 == 0:
        counter_2 += 1
    if n % 10 > 5:
        j = n % 10
        counter_sum_5 += j
    if n % 10 > 7:
        f = n % 10
        counter_num_7 *= f
    if n % 10 == 5 or n % 10 == 0:
        counter_num_0 += 1
    n //= 10
print(counter_3)
print(counter_last)
print(counter_2)
print(counter_sum_5)
print(counter_num_7)
print(counter_num_0)
