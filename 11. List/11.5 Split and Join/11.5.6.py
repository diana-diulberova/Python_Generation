s = input()
numbers = s.split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
    print('+' * (numbers[i]), sep='\n')
