txt = "комп'ютер"

t = """sumary_line
Keyword arguments:
argument -- description
Return: return_description
"""

n = 15
to_str = str(n)
# print(n)
# print(type(to_str))

s = str([1,2,3,4,5])
# print(s)


S = 'ABCDEFG'
# print(S[0])
# print(S[-1])
# print(S[3])

# Создать строку, которая состоит из имени и фамилии ученика (Ivanov Ivan).
# Сравнить, совпадает ли первая буква имени с первой буквой фамилии и вывести соответствующее сообщение.
# При получении буквы фамилии использовать отрицательный индекс.

name = 'Ivan Ivanov'
surname = name[-6]
firstname = name[0]

# if surname == firstname:
#     print('Sovpadaet')
# else:
#     print('ne sovpadaet')

# slice[start : end : step]

s = 'abcdefghijk'
# print(s[3:6])
# print(s[:])
# print(s[:6])
# print(s[3:])
# print(s[::-1])
# print(s[-3:])
# print(s[:-3])
# print(s[::2])


s = 'hello'
# s[0] = 'k'
# print(s)

t1 = 'Hello'
t2 = 'World'
t3 = t1 + ' ' + t2
# print(t3)

t4 = '-' * 5
# print(t4)


y = 'lorem ipsum \ndolores'
# print(y)

song = 'Jingle bells, jingle bells Jingle all the way Oh, what fun it is to ride In a one horse open sleigh'

# print(len(song))

a = '12 .@#345'
# print(len(a))

for char in song:
    print(char, end=' ')