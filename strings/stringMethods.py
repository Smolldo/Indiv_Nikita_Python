# count(element, start, end) - посчитивание количества елемента в строке

p = 'Lomem ipmsum'
# print(p.count('m', 0, 5))

s = 'loRem ipSUM'
# .upper() - делает ВСЕ символо большими (верхний регистр)
print(s.upper())

# .lower() - делает символи маленькими
print(s.lower())

# .title() - делает 1 букву каждого слова большой
print(s.title())

#.capitalize() - 1 буква первого слова большая. ВСЕ остальное маленькое
print(s.capitalize())

# .find() - ищет елемент. возвращает индекс начала елемента
d = 'Hello World!'

# print(d.find('tree'))
print(d.rfind('o'))


# Ввести произвольное сообщение с клавиатуры. Если в сообщении встречаются слова «купить», 
# «продать», «реклама», то пометить это сообщение как спам.

spam = ['продать', 'купить', 'реклама']

# msg = input('>')

# for i in spam:
#     if msg.find(i) != -1:
#       print('spam detected')
#       break
# else:
#     print('no spam')



# .split() - разделяет строку по разделителю и превращает в список
s = "I am learning strings in Python. Some new methods got now."
s1 = s.split('. ')
# print(s1)


# .join() - со списка делает строку
sentences = ["I am learning strings in Python", "Some new methods got now."]
s2 = '. '.join(sentences)
# print(s2)


# .strip() - убрать пробе в начале и конце строки

f = ' lol '
print(f.strip())


# .replace(old, new) - заменяет старий елемент на новий

p = 'Hello world'
p1 = p.replace('world', 'python')
print(p1)

print(f'sdfsdfsdf {p1}')