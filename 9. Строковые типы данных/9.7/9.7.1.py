# Используя метод format(), дополните приведенный код так, чтобы он вывел текст:

# In 2010, someone paid 10k Bitcoin for two pizzas.

year = 2010
a = '10k'
b = 'Bitcoin'

s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, a, b)

print(s)
