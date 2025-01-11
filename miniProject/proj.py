import random

# randint - случайное целое число  choice


a = random.randint(1, 9)


print(random.randint(1, 9))
print(random.randint(1, 9))
print(random.randint(1, 9))
print(random.randint(1, 9))
print(random.randint(1, 9))


from colorama import Fore, Back, Style

# print(Fore.CYAN + "This is cyan text")
# print(Back.GREEN + Fore.RED +'this text has green back')
# print(Style.DIM + Back.BLUE + 'this is dim text')


name = 'John'
print(Fore.CYAN + 'Hello! ' + Fore.YELLOW + name + Style.RESET_ALL)


