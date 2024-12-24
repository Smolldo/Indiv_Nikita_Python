age = 8

# if age >= 18:
#     print('adult')
# else:
#     print('kid')

# a = 0

# if a > 0:
#     print('positive')
# elif a < 0:
#     print('negative')
# else:
#     print('a = 0')


# grade = 71


# if grade >= 80:
#     print('A')
# elif grade >= 70:
#     print('B')
# elif grade >= 60:
#     print('C')
# else:
#     print('error')

# 0 - False, None - False,  [], '', {} -False,  все остальное - True

# if True:
#     pass


b = ' '

# if b:
#     print(True)

# money = 4.55

# if money:
#     print(f'u have ${money}')
# else:
#     print('u have no money')

# age = 18
# lic = False

# if age >= 16 and lic:
#     print('u can drive')
# else:
#     print('u cant drive')


# and - i,  or - либо, not - не

# front_door = True
# back_door = False

# if front_door or back_door:
#     print('u r in')
# else:
#     print('NO')

# f = 5

# n = True if f > 0 else False
# if f > 0:
#     print(True)
# else:
#     print(False)
# print(n)

x = 6

res = 'Parnoe' if x % 2 == 0 else 'Ne parnoe'
# print(res)

o = 6

result = 'Zdal' if o >= 6 and o <=10 else 'Ne zdal'
# print(result)


x = 6
y = 3

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')
elif x == 0 and y == 0:
    print('tochka na 0')
else:
    print('error')