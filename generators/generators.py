def count_down(n):
    while n > 0:
        yield n
        n -= 1

num = count_down(5)

# print(next(num))
# print(next(num))


numbers = (x*x for x in range(10) if x % 2 ==0)

# print(next(numbers))
# print(next(numbers))


# Знайти квадрати парних чисел у списку
n = [1,2,3,4,5,6,7,8]

squares = (x*x for x in n if x % 2 ==0)

# for i in squares:
#     print(i)


# Генерувати нескінченну послідовність починаючи з певного числа

def infinity(start):
    while True:
        yield start
        start += 1

sequence = infinity(10)

# print(next(sequence))
# print(next(sequence))
# print(next(sequence))
# print(next(sequence))

# Вычисление суммы всех четных чисел в списке

chisla = [1,2,3,4,5,6,7,8,9,10]

