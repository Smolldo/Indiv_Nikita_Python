# try:
#     with open('input.txt', 'r') as file:
#         data = file.read()
# except FileNotFoundError:
#     print('file not found((((')
# except IOError:
#     print('access error. need a password')
# else:
#     print('file readed!')
#     print(data)
# finally:
#     print('operation completed!')


# try:
#     num = int(input('Enter num: '))
# except ValueError:
#     print('this is not a number. try again!')
# else:
#     res = num ** 2
#     print(f'result = {res}')
# finally:
#     print('operation completed!')


# class MyCustomError(Exception):
#     def __init__(self, message = 'возникла ошибка'):
#         self.message = message
#         super().__init__(self.message)

# try:
#     raise MyCustomError('smthng wrong!')
# except MyCustomError as e:
#     print(f'my own exception: {e}')

# def divide_numbers(a, b):
#     try:
#         c = a / b
#     except ZeroDivisionError as e:
#         print(f'error. cant division by zero: {e}')
#         return None
#     return c

# def process_division(a, b):
#     try:
#         result = divide_numbers(a,b)
#         if result is not None:
#             print(result)
#     except Exception as e:
#         print(f'unknown error: {e}')


# process_division(10, 2)


import logging


logging.basicConfig(level= logging.ERROR, filename= 'app.log', filemode= 'a', format= "%(asctime)s - %(levelname)s - %(message)s")


def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error('Ошибка деления на 0', exc_info= True)
    except TypeError as e:
        logging.error('no no no bukvi', exc_info= True)

divide_numbers(10, 0)





