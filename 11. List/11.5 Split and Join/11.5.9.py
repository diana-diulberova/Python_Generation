s = input()
count = 0

num = s.split()

for i in range(len(num)):
    for j in range(i+1, len(num)):
        if num[i] == num[j]:
            count += 1

print(count)
