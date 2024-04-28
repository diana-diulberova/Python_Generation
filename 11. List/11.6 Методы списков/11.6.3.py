str = input()
s = str.lower()
text = s.split()

a = text.count('a')
an = text.count('an')
the = text.count('the')

print(f'Общее количество артиклей: {a+an+the}')
