s = input()
words = s.split()
list = []

for i in range(len(words)):
    a = int(words[i])
    list.append(a)

num_min = min(list)
index_min = list.index(num_min)

num_max = max(list)
index_max = list.index(num_max)

list.insert(index_max, num_min)
list.pop(index_max + 1)

list.insert(index_min, num_max)
list.pop(index_min + 1)

print(*list)
