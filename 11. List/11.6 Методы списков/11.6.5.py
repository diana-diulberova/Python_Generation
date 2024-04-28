s = input()
numbers = s.split()

numbers.sort(key=int)
print(*numbers)
numbers.sort(reverse=True, key=int)
print(*numbers)
