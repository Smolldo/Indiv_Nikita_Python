a = lambda x: x * 3

# print(a(3))

def multiply(x):
    return x * 3


max_num = lambda a, b: a if a > b else b
# print(max_num(7,4))

nums = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, nums))
# print(squared)


# Создайте лямбда-функцию для вычисления куба числа.
n = lambda x: x ** 3
# print(n(2))


# Напишите лямбда-функцию, которая проверяет, является ли одно число кратным другому, и проверьте ее для разных пар чисел.

kratn  = lambda x, y: x % y == 0
# print(kratn(2, 2))


# Создайте лямбда-функцию для вычисления среднего арифметического двух чисел. 

average = lambda x, y: (x + y) / 2
# print(average(2,5))

# Используя теорему Пифагора, создайте лямбда-функцию для вычисления длины гипотенузы прямоугольного треугольника по данным катетам. 

# a2 + b2 = c2
# c = sqrt(a2 + b2)
import math

c = lambda a, b:  math.sqrt(a ** 2 + b ** 2)

print(c(8,14))

