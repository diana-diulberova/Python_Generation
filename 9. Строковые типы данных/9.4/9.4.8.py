s = input()

a = s.find('h')
b = s.rfind('h')

s_new = s[:a] + s[b+1:]

print(s_new)
