numbers = [8, 9, 10, 11]

# task_1_1 = numbers.pop(1)
# task_1_2 = task_1_1.insert(1, '17')

numbers[1] = 17
numbers.extend([4, 5, 6])

# numbers.pop(0)
del numbers[0]

numbers *= 2

numbers.insert(3, 25)


print(numbers)
