a = 2
b = 0

try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print('division by zero')

# print('aaaaaa')


# try:
#     number = int(input('Enter integer: '))
#     print(f'you entered: {number}')
# except ValueError:
#     print('enter only numbers')


try:
    with open('input.txt', 'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print('file not found(')




# try:
#     value = int(input('Enter some number: '))
#     result = 10 / value
#     print(f'result = {result}')

# except ValueError:
#     print('only numbers!!!!!')
# except ZeroDivisionError:
#     print('not 0!!!!!!')


# try:
#     numbers = [10, 20, 30]
#     index = int(input('Enter some index: '))
#     result = 100 / numbers[index]
#     print(f'result = {result}')

# except ValueError:
#     print('only numbers!!!!!')
# except ZeroDivisionError:
#     print('not 0!!!!!!')
# except IndexError:
#     print('index out of range!')


try:
    with open('input.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('file not found')
finally:
    print('file closed')



def div(a,b):
    if b == 0:
        raise ZeroDivisionError('error. dib by 0 = !!!!!!')
    return a / b

try:
    result = div(10, 0)
except ZeroDivisionError as e:
    print(e)