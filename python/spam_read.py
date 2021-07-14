# Напишите программу, которая фильтрует спам, поступающий на
# корпоративную почту. Спам – письма, в тексте которых часть букв в
# словах заменена на цифры. На вход подается файл с сообщениями.
# Выход – файл без спам-писем.
# Программа должна работать с файлами, размер которых превышает
# объем оперативной памяти. Файл подается в виде текстового файла.  Одно письмо = одна строка. 

def is_spam(line):
    words = line.split()
    for word in words:
        contains_digit = any(symbol.isdigit() for symbol in word)
        contains_letter = any(symbol.isalpha() for symbol in word)
        if contains_digit and contains_letter: 
            return True
    return False

def filter_spam(input_file, output_file):
    with open(input_file, 'r') as f, open(output_file, 'w') as g:
        for line in f:
            if not is_spam(line):
                g.write(line)


if __name__ == '__main__':
    filter_spam('spam.txt', 'no_spam.txt')

