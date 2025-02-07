# slice(start : end : step)


l = [1,2,3,4,5,6,7,8,9]

# print(l[2:6])
# print(l[3:6])
# print(l[:])
# print(l[:6])
# print(l[3:])
# print(l[::-1])
# print(l[-3:])
# print(l[:-3])
# print(l[::2])


# Дан список: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Используя срезы, вывести на экран все четные числа.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Задан список номеров мобильных телефонов: phones = ['+38(067) 999-99-99', '+38(066) 999-99-99-99','+38(067) 888-88-88', 
# '+38(068) 777-77-77'] Считая, что все номера записаны в формате +38 (код) 111-11-11, 
# посчитать количество абонентов оператора, имеющего коды «067», «097», «068»

phones = ['+38(067) 999-99-99', '+38(066) 999-99-99-99','+38(067) 888-88-88', '+38(068) 777-77-77']

operator = ['067', '097', '068']

count = 0

for i in phones:
    code = i[4:7]
    if code in operator:
        count += 1

# print(count)



#множества  -  set()

a = set('hello')
# print(a)

b = {1,2,3,4,5,6,7}

c = {
    'name': 'John',
    'age': 23
}



# add() - добавляет елемент в множество

b = {1,2,3,4,5,6,7}

b.add(0)

# print(b)


# remove() - удаляет елемент. возвращает ошибку если такого елемента нету

b.remove(6)
print(b)


# discard() - удаляет елемент. НЕ возвращает ошибку если такого елемента нету

b.discard(10)
print(b)


# pop() - удаляет первьІй елемент с множества
b.pop()
print(b)




a = set('hello') 

b = set('hi there!')

# union

# print(a.union(b))
# print(a | b)


#intersection

# print(a.intersection(b))
# print(a & b)


# difference

print(b.difference(a))


# symmetric_difference

print(a.symmetric_difference(b))
print(a ^ b)