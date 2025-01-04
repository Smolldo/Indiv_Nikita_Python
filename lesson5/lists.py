a = [1, 2, 3, 2.3, 'adjhsdf', True, (1,2,3), {1: 3}]

b = []

d = list('dsfhju sdfjoss sfuoisdf sfuiosd sfuisd')
# print(d)

products = ['milk', 'cheese', 'bread', 'coke', 'chips']

# print(products[0]) #milk
# print(products[-1]) #chips
# print(products[2]) #bread

L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']

# print(L[2][2][1])

# Написать программу, которая считает сумму всех элементов в списке.

q = [1, 2, 3, 4, 5]

suma = 0

for i in q:
    suma += i


# Написать программу, которая получает максимальное число из списка.

lst = [1, 34, 2, 56, 999, 12, 76, 555, 19]

max_num = lst[0]

for i in lst:
    if i > max_num:
        max_num = i
# print(max_num)

# Возвести каждый из элементов списка к кубу

lst1 = [1,2,3,4,5]
# i ** 3

# for i in lst1:
#     print(i ** 3)


# Написать программу, которая уберет дубликаты из списка.
# .append()
lst2 = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6, 6]

uniq = []

for i in lst2:
    if i not in uniq:
        uniq.append(i)

print(uniq)


