# fl = open('fileswork/test.txt', 'r')

# for line in fl:
#     print(line)

# print(fl.read())

# fl = open('text.txt', 'a')

# fl.write('\nThis is third sentence')


# fl.close()


# with open('text.txt', 'w') as fl:
#     fl.write('Hello')


# Напишіть програму, яка зчитує вміст файлу "input.txt" і записує його у файл "output.txt"
#  з виключенням повторюваних рядків.

lines = ['cat', 'dog', 'cat', 'mouse']

with open('input.txt', 'w') as inp:
    for line in lines:
        inp.write(line + '\n')

uniq = []

with open('input.txt', 'r') as inp:
    for line in inp:
        if line in uniq:
            continue
        else:
            uniq.append(line)


with open('output.txt', 'w') as out:
    out.writelines(uniq)


# Напишите функцию, которая принимает путь к файлу в качестве аргумента и возвращает количество строк в файле.

def count_lines(file_name):
    with open(file_name, 'r') as fl:
        return sum(1 for line in fl)
    

print(count_lines('input.txt'))