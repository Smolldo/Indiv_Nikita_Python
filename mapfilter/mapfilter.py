# map(func, iter)


nums = [1,2,3,4,5]

squared = map(lambda x: x ** 2, nums)

# print(list(squared))

words = ['hello', 'world', 'python']

up = map(lambda x: x.upper(), words)

# print(list(up))


# filter(func, iter)

def is_even(n):
    return n % 2 == 0


nums = [1,2,3,4,5,6,7,8,9]

even = list(filter(is_even, nums))
# print(even)

text = ['apple', '', 'banana', ' lemon', ' orange ']

# not_empty = list(filter(lambda x: x != '', text))

not_empty = list(filter(lambda x: x.strip(), text))

# print(not_empty)


n1 = [1,2,3,4,5]
n2 = ['a', 'b', 'c']

def triple(n):
    tri = list(map(lambda x: x * 3, n))
    return tri

# print(triple(n1))
# print(triple(n2))

# Вам дано предложение в виде строки. Разделите предложение на слова и используйте map для создания списка, 
# содержащего длины каждого слова в предложении.

s1 = 'hello world python computer'

words = s1.split()

lengths = list(map(lambda x: len(x), words))

print(lengths)
