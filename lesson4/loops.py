text = 'apple'

# for i in text:
#     print(i)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = 0


# for n in nums:
#     suma += n #  suma = suma + n

# print(suma)

colors = ['red', 'green', 'blue', 'yellow']

# for i in colors:
#     print(i)
# else:
#     print('Done!')



#range(start, end, step)  - промежуток


# for i in range(1, 11, 4):
#     print(i)


# for i in range(10):
#     for j in range(10, 20):
#         print(i,j)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())


# print(end = '\t')
# for i in range(c, d + 1):
#     print(i, end= '\t')
# print(' ')

# for i in range(a, b + 1):
#     print(i, end='\t')
#     for j in range(c, d + 1):
#         print(i * j, end='\t')
#     print(' ')



a = 1

# while a < 5:
#     print(a)
#     a+=1

# a = 1
# while True:
#     print(a)
#     if a == 20:
#         break
#     a += 1

b = 0

while b <= 20:
    b+=1
    if b % 2:
        continue
    print(b)