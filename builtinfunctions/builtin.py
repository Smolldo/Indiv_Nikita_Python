
numbers = [1,2,3,4,5,6,7,8,9, -1]

all_positives = all(n > 0 for n in numbers)

# print(all_positives)

words = ['apple', 'banana', 'coconut', '']

not_empty = all(words)

# print(not_empty)


nums = [-1, 0, -2, 2]

has_positive = any(n > 0 for n in nums)

# print(has_positive)

words = ["apple", "banana", "Cherry", "date"]

has_capital = any(word[0].isupper() for word in words)

# print(has_capital)



# sorted(iterable, key = None, reverse  = False)

numbers = [8,1,5,2,8,3,9,3,0]

sorted_nums = sorted(numbers, reverse=True)

# print(sorted_nums)


tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]

sorted_tuples = sorted(tuples, key= lambda x: x[0])

# print(sorted_tuples)

# Напишите программу, которая позволяет пользователю ввести строку символов и использовать any() 
# для проверки, содержит ли строка любые гласные буквы. Выведите результат проверки.

vowels = 'eioauy'

text = input('Enter some text: ')

contain_vowels = any(char in vowels for char in text)

print(contain_vowels)

