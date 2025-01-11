a= [1,2,3,4,5,6,7,8,9]

#slice - срез [start : end: step]

# print(a[1:9])

# .append() - вставляет елемент в конец списка

lst = ['a', 'b']

lst.append('c')

# print(lst)


# .remove() - удаляет елемент со списка, возвращает ошибку, если такого елемента нет в списке

# lst = ['a', 'b', 'b']

# lst.remove('b')

# print(lst)


# .pop() - удаляет елемент со списка по ИНДЕКСУ, по умолчанию удаляет последний елемент.

# lst = ['a', 'b', 'c']

# lst.pop()

# print(lst)


# del - удалить

lst = ['a', 'b', 'c']

# del lst[2]

# print(lst)



# .extend() - расширить

a = [1,2,3,4]
b = [5,6,7,8]

# a.extend(b)

# print(a)


# .insert() - вставить, вложить

a = ['a', 'b']

a.insert(1, 'hello')

# print(a)


# .clear() - очищает список

d = [1,2,3,4,5]
# print(d)
# d.clear()
# print(d)


# .index() - показивает индекс елемента по значению
chars = ['a', 'b', 'c', 'd']

# print(chars.index('c'))


#  .count() - подсчитивает количество конкретного елемента

chars = ['a', 'b', 'c', 'a']

# print(chars.count('a'))


#  .sort() - сортирует

t = [1,7,3,7,9,4,2,6]
# t.sort(reverse=True) - в обратном порядку
# t.sort() # в обичном порядке

# print(t)

# print(sorted(t))


# .reverse() - переворачивает. НЕ СОРТИРУЕТ

u = [1,2,3,4,5,6]
u.reverse()
# print(u)


# .copy() - копирует список

m = [1,2,3]
# n = m.copy()

# print(n == m)

# len() - длина списка
u = [1,2,3,4,5,6]

# print(len(u))

chars = ['a', 'b', 'c', 'd']

# if 'g' in chars:
#     print('YES')
# else:
#     print('Noo')


fruits = ['apple', 'banana', 'cherry']

# for i, fruit in enumerate(fruits, start=1):
#     print(i, fruit)



# Создать список, который содержит элементы исходного списка на четных позициях. 
# Используйте enumerate для итерации по списку и выборки элементов с четным индексом.

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

result = []

for index, num in enumerate(numbers):
    if index % 2 == 0:
        result.append(num)

print(result)
