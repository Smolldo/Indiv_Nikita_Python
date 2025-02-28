d1 = dict()

d2 = {1,2,3,4}

d3 = {
    'name': 'John',
    'age': 26,
    3: 123
}



#get
a = d3.get('city', 'No key')
print(a)

# добавление елемента

d3['city'] = 'Kyiv'

print(d3)


#pop

d3.pop(3)
print(d3)


#clear()

# d3.clear()
# print(d3)

# update()

d3.update({'email': 'fdghdjfg@gmail.com'})
print(d3)


#copy()

d4 = d3.copy()
print(d3 == d4)


# Напишите программу, которая позволяет пользователям регистрироваться на сайте и сохраняет их данные в словаре. 
# Ключ - имя пользователя, а значение - пароль.

login = input('Enter your login: ')
password = input('Enter your password:')

users = {}

users[login] = password

print(users)