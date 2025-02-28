nums = {
    1: 'one',
    2: 'two',
    3: 'three'
}

# for i in nums:
#     print(i)

# for i in nums.keys():
#     print(i)

# for i in nums.values():
#     print(i)

# for key, value in nums.items():
#     print(key, value)

transport = {
    'AA1111AA': 'Іванов Іван',
    'IVANOV'  : 'Іванов Іван',
    'AA0007AA': 'Семенов Андрій',
    'AA007AA' : 'Іванов Іван',
    'AВ1111AВ': 'Вінниця Водоканал',
    'AІ1010КК': 'Семенов Андрій',
}

transport['BE0988BP'] = 'Петренко Петро'
transport['73811HI'] = 'Artur Morgan'

# print(transport['9999'])

searched = transport.get('73811HI', 'No auto')
# print(searched)

car_owners = {}

for i in transport.values():
    car_owners[i] = car_owners.get(i, 0) + 1

# print(car_owners)

# Создайте словарь «stock», который будет содержать в себе 
# (ключ - название товара. Значение - количество товара на складе). Написать программу, 
# которая спрашивает какой товар и количество, которое хочет купить пользователь. Вывести на экран True,
#  если пользователь может купить этот товар, если нет 

stock = {
    'RTX5090': 200,
    'PIZZA': 420,
    'COCA-COLA': 3
}

product = input('Enter product: ')
amount = int(input('Enter amount: '))

if product in stock and stock[product] >= amount:
    print(True)
else:
    print(False)