def total(*numbers):
    for i in numbers:
        print(i)


# total(1,2,3,4,5)



def humans(**people):
    for name, year in people.items():
        print(name, year)


# humans(John = 1986, Jack = 1999)


# Написати функцію, яка приймає рядок і повертає кількість голосних букв у цьому рядку.

vovels = 'euoayi'
# inp = input('Enter smth: ').lower()


def glasnie(txt):
    count = 0
    for i in txt:
        if i in vovels:
            count += 1
    return count

# print(glasnie(inp))

# Написать функцию, которая принимает список чисел и возвращает наибольшее число в этом списке.

l1 = [1,2,3, 22 ,4,5,6]

def prmax(lst):
    return max(lst)

print(prmax(l1))

# Написать функцию, которая принимает список и возвращает список, содержащий только уникальные элементы исходного списка.
# list()  set()


# print(list(set(l2)))

l2 = [1,1,1,2,2,2,3,3,3,]


def uniqs(lst):
    uniqList = []

    for i in lst:
        if i not in uniqList:
            uniqList.append(i)
        else:
            continue
    return uniqList

# print(uniqs(l2))



# Написать функцию, которая принимает список и возвращает список, состоящий из элементов входного списка в обратном порядке.

l1 = [1,2,3, 22 ,4,5,6]

def rvrs(lst):
    return lst[::-1]

print(rvrs(l1))