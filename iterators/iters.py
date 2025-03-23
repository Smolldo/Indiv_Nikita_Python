def __iter__(self):
    return self

def __next__(self):
    raise StopIteration


class CountDown:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num
        
cd = CountDown(5)

# for num in cd:
#     print(num)
    
# print(next(cd))
# print(next(cd)) 
# print(next(cd)) 
# print(next(cd)) 
# print(next(cd)) 
# print(next(cd)) 

from itertools import count

counter = count(start= 5)

# print(next(counter))
# print(next(counter))
# print(next(counter))


# Створіть ітератор, який буде ітерувати по кожному символу у заданому рядку.

class StringIterator:
    def __init__(self, string):
        self.string = string
        self.index = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.string):
            char = self.string[self.index]
            self.index += 1
            return char
        raise StopIteration
    
# for char in StringIterator('Hello'):
#     print(char)


# Створіть ітератор, який повертає елементи списку у зворотному порядку.

class ReversIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.data[self.index]
        raise StopIteration
    
for char in ReversIterator('Hello'):
    print(char)