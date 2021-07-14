# скрипт для генерации файла писем со спамом для отладки задачи поиска спама
# generate big file

import random

ab = list(map(chr, range(97, 123)))
ab_d = ab + '1 2 3 4 5 6 7 8 9'.split()
print(ab)


with open('spam.txt', 'w') as f:
    for k in range(int(1e2)):
       str_len = random.randrange(2, 150)
       my_str = ''
       my_spam_str = ''
       for i in range(str_len):
           word_len = random.randrange(2, 7)
           my_str += ''.join(random.choices(ab, k = word_len)) + ' '
           my_spam_str += ''.join(random.choices(ab_d, k = word_len)) + ' '
       print(my_str)
       print(my_spam_str)
       f.write(my_str[:-1] + '\n')
       f.write(my_spam_str[:-1] + '\n')


