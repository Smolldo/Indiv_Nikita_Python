# Завдання 1 - Видалення дублікатів слів у рядку

def remove_duplicates(s):
    words = s.split()
    uniq_words = set(words)

    return ' '.join(uniq_words)

s1 = 'Hello world python python world banana'

print(remove_duplicates(s1))



# Завдання 2 - Перевірка кількості цифр у рядку
def counter(s):
    return sum(1 for i in s if i.isdigit())


s2 = 'ghsdyg3yifdhig45uivsdfui757352hdifghdfuio'

print(counter(s2))


# Завдання 4 - Перевірка на паліндром

def is_palindrome(s):
    cleaned = ''.join(i.lower() for i in s if i.isalnum())
    return cleaned == cleaned[::-1]


s3 = 'Bird rib'
print(is_palindrome(s3))