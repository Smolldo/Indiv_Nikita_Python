def add(a, b):
    print(a + b)


def printHello():
    print('Hello word')

# printHello()

# add(3, 5)
# add(6, 8)


def plus(a, b):
    return a + b


a = 12 + plus(4,5)
# print(a)



x = 50

def func():
    x = 2
    print('меняем локального х на', x)

# func()
# print('х как и бил = ', x)


x = 50

def fun():
    global x
    print('x = ', x)
    x = 2
    print('меняем х на х = ', x)

# fun()
# print('х поменялось на х = ', x)

def test(a, b = 5, c = 10):
    print(f'a = {a} \n b = {b} \n c = {c}')

# test(10)
# test(3, 7, 9)
# test(4, b = 6)
# test(3, c = 8, b = 7)


def repl(msg, times = 5):
    print(msg * times)

repl('Hello')