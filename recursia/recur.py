def recursive_search(lst, itm):
    if lst[0] == itm:
        return True
    else:
        return recursive_search(lst[1:], itm)
    
# print(recursive_search([1,2,3,4,5,6,7], 4))



# Вам нужно написать рекурсивную функцию, которая вычисляет сумму всех натуральных чисел от 1 до N, 
# где N - это неотрицательное целое число, переданное в качестве аргумента функции.


def suma(n):
    if n == 0:
        return 0
    return n + suma(n - 1)


# N = 5
# if N < 0:
#     print('error')
# else:
#     print(suma(N))

# Напишите рекурсивную функцию, которая подсчитывает, сколько раз символ «x» встречается в данной строке. 
# Функция должна быть чувствительной к регистру.

def count_x(e):
    if len(e) == 0:
        return 0
    return (1 if e[0] == 'x' else 0) + count_x(e[1:])

t = 'ggygyxiokopkoiklxtfytrjfutykjx'

# print(count_x(t))


# Создайте рекурсивную функцию, которая принимает строку в качестве аргумента и возвращает эту 
# строку в обратном порядке. Попробуйте не использовать срезы строк или циклы.

