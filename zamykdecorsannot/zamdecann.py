def out_func(x):
    def inner_func(y):
        return x + y
    return inner_func

clos = out_func(5)
print(clos(10))


def my_counter():
    counter = 0
    def inner_func():
        nonlocal counter
        counter += 1
        return counter
    return inner_func


cou = my_counter()

# print(cou())
# print(cou())
# print(cou())
# print(cou())
# print(cou())

def multiplier(x):
    def mult_by(y):
        return x * y
    return mult_by

mult = multiplier(5)
# print(mult(2))



# @decorator_name
# def func_to_decorate():
#     pass


def logger(func):
    def wrapper():
        print(f'vizivaetsa funkciia: {func.__name__}')
        return func()
    return wrapper


@logger
def say_hi():
    print('Hello world')

# say_hi()


def greet(name: str, age: int) -> tuple[str, int]:
    return f'hello {name}. {age}'

# print(greet('John', 23))
# print(greet(12, 23))

from typing import List, Dict, Set, Tuple, Callable

names: List[str] = ["Alice", "Bob", "Charlie"]
scores: Dict[str, int] = {"Alice": 10, "Bob": 15, "Charlie": 8}
unique_numbers: Set[int] = {1, 2, 3, 4}
coordinates: Tuple[int, int, int] = (10, -2, 0)


def aaply_operation(operation: Callable[[int, int], int], a: int, b: int) -> int:
    return a + b

def add(a: int, b: int) -> int:
    return a + b

# int a, b,c,d
# a = 7

result = aaply_operation(add, 5, 7)
print(result)