# s = '    Python rocks!     '
# print(s.strip())


# s = 'Python rocks!'
# print(s.replace('o', '@'))


# s = input()
# s_new = ''

# for i in range(len(s)):
#     if i % 3 != 0:
#         s_new += s[i]
# print(s_new)


# s = input()
# print(s.replace('1', 'one'))


# s = input()
# s_new = ''

# for i in range(len(s)):
#     if s[i] != '@':
#         s_new += s[i]
# print(s_new)


# s = input()
# res = s.replace("@", "")

# print(res)


# s = input()
# count = 0

# for i in range(len(s)):
#     if s[i] == 'f':
#         count += 1
#         if count == 2:
#             print(i)
#             break

# if count == 0:
#     print(-2)
# elif count == 1:
#     print(-1)


s = input()
s1 = s[:s.find('h')+1]
s_new = s[s.find('h')+1:s.rfind('h')]
s2 = s[s.rfind('h'):]

print(s1+s_new[::-1]+s2)
