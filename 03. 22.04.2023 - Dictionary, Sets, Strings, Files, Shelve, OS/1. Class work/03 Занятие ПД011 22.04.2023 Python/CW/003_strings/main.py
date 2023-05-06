# Строка представляет последовательность символов в кодировке Unicode.
# Строка не изменяема
# Можно обратиться к отдельным символам строки по индексу
# в квадратных скобках:
string = "hello world, мир!"
print(string)
print('012345678901234567890')
print('          1         2')
c0 = string[0]  # h
print(c0)
c6 = string[6]  # w
print(c6)


# раскомментировать для формирования ошибки
# c101 = string[101]  # ошибка IndexError: string index out of range
# print(c101)

# Индексация начинается с нуля, поэтому первый символ строки будет
# иметь индекс 0. Если мы попытаемся обратиться к индексу, которого
# нет в строке, то мы получим исключение IndexError. 

# Чтобы получить доступ к символам, начиная с конца строки, можно использовать
# отрицательные индексы. Так, индекс -1 будет представлять последний символ,
# а -2 - предпоследний символ и так далее:
string = "hello world"
print(string)
print('012345678901234567890')
print('          1         2')
c1 = string[-1]  # d
print(c1)
c5 = string[-5]  # w
print(c5)

# При работе с символами следует учитывать, что строка - это неизменяемый (immutable)
# тип, поэтому если мы попробуем изменить какой-то отдельный символ строки, то мы получим
# ошибку, как в следующем примере:
# string = "hello world"
# string[1] = "R"
# Мы можем только полностью переустановить значение строки, присвоив ей другое значение.
string += "К"
print(string)


# Получение подстроки
# При необходимости мы можем получить из строки не только отдельные символы, но и подстроку.
# Для этого используется следующий синтаксис (срезы строки):
# string[:end]           : извлекается последовательность символов начиная с 0-го индекса по индекс end
# string[start:end]      : извлекается последовательность символов начиная с индекса start по индекс end
# string[start:end:step] : извлекается последовательность символов начиная с индекса start
#                          по индекс end через шаг step (текущий символ входит в шаг)

# Используем все варианты получения подстроки:
string = "hello world"

# с 0 до 5 символа
sub_string1 = string[:5]
print(sub_string1)      # hello

# со 2 до 5 символа
sub_string2 = string[2:5]
print(sub_string2)      # llo

# со 2 по 9 символ через один символ
# Hello world
# 01234567890
#   . . . .
sub_string3 = string[2:9:2]
print(sub_string3)      # lowr


# Функции ord и len
# Поскольку строка содержит символы Unicode, то с помощью функции ord() мы
# можем получить числовое значение для символа в кодировке Unicode:
print(ord("A"))     # 65

# Для получения длины строки можно использовать функцию len():
string = "hello world"
length = len(string)
print(length)   # 11

# Поиск в строке
# С помощью выражения term in string можно найти подстроку term в строке string.
# Если подстрока найдена, то выражение вернет значение True, иначе возвращается значение False:
print('\nПоиск в строке')
string = "hello world"
key = 'hello'
exist = key in string
print(f'"{key}" in {string}: {exist}')     # True

key = 'sword'
exist = key in string
print(f'"{key}" in {string}: {exist}')    # False

exist = key not in string
print(f'"{key}" not in {string}: {exist}')    # True


# Перебор строки
# С помощью цикла for можно перебрать все символы строки:
print('\nПеребор строки: ', end='')
string = "hello world"
for char in string:
    print(char, end=' ')
print()


# пример перебора и поиска в строке
# подсчет в строке количества цифр
string = 'сегодня 13.03, весна 2022'
cntDigits = 0
digits = '0123456789'

for ch in string:
    if ch in digits:
        cntDigits += 1
print(f'В строке "{string}" найдено цифр: {cntDigits}')


# Рассмотрим основные методы строк, которые мы можем применить в приложениях:
#
# isalpha()  : возвращает True, если строка состоит только из алфавитных символов
# islower()  : возвращает True, если строка состоит только из символов в нижнем регистре
# isupper()  : возвращает True, если все символы строки в верхнем регистре
# isdigit()  : возвращает True, если все символы строки - цифры
# isnumeric(): возвращает True, если строка представляет собой число

print('\nОсновные методы строк')
string = input("isnumber(). Введите число: ")
if string.isnumeric():
    number = int(string)
    print(number)
# end if


# startswith(str): возвращает True, если строка начинается с подстроки str
# endswith(str)  : возвращает True, если строка заканчивается на подстроку str
file_name = "hello_first.py"

key = "hello"
starts_with_hello = file_name.startswith(key)  # True
print(f'"{file_name}".startswith("{key}"): {starts_with_hello}')

key = "exe"
ends_with_exe = file_name.endswith(key)          # False
print(f'"{file_name}".endswith("{key}"): {ends_with_exe}')

# lower()     : переводит строку в нижний регистр
# upper()     : переводит строку в вехний регистр
# title()     : Начальные Символы Всех Слов В Строке Переводятся В Верхний Регистр
# capitalize(): Переводит в верхний регистр первую букву только самого первого слова строки

# lstrip(): удаляет начальные пробелы из строки
# rstrip(): удаляет конечные пробелы из строки
# strip() : удаляет начальные и конечные пробелы из строки
string = "   hello   happy    world!  "
print('\nУдаление начальных, хвостовых или и начальных и хвостовых пробелов')
print(f"\nИсходная строка: '{string}'")
string = string.strip()
print(f"string.strip(): '{string}'\n")

string = "   hello   happy    world!  "
print(f"Исходная строка: '{string}'")
string = string.lstrip()
print(f"string.lstrip(): '{string}'\n")

string = "   hello   happy    world!  "
print(f"Исходная строка: '{string}'")
string = string.rstrip()
print(f"string.rstrip(): '{string}'\n")

# ljust(width): если длина строки меньше параметра width, то справа от строки
#               добавляются пробелы, чтобы дополнить значение width, а сама
#               строка выравнивается по левому краю
# rjust(width): если длина строки меньше параметра width, то слева от строки
#               добавляются пробелы, чтобы дополнить значение width, а сама
#               строка выравнивается по правому краю
# center(width): если длина строки меньше параметра width, то слева и справа от
#                строки равномерно добавляются пробелы, чтобы дополнить значение
#                width, а сама строка выравнивается по центру

print('\nВыравнивание текста:')
print(f'ljust(12) : "{"36000".ljust(10)}"')
print(f'center(12): "{"36000".center(10)}"')
print(f'rjust(12) : "{"36000".rjust(10)}"')
print()


# find(str[, start [, end]): возвращает индекс подстроки в строке. Если подстрока
#                            не найдена, возвращается число -1
print('Поиск подстроки в строке find()')
welcome = "Hello world! Goodbye world!"
key = 'wor'
index = welcome.find(key)
print(f'"{welcome}".find("{key}"): {index}')  # 6

# поиск с 10-го индекса
index = welcome.find(key, 10)
print(f'"{welcome}".find("{key}", 10): {index}')  # 21

# поиск с 10 по 15 индекс
index = welcome.find("wor", 10, 15)
print(f'"{welcome}".find("{key}", 10, 15): {index}')  # 21
print()


# replace(old, new[, num]):  заменяет в строке одну подстроку на другую
print('\nreplace(): заменяет в строке одну подстроку на другую')
phone = "+1-234-567-89-10"

# замена дефисов на пробел
edited_phone = phone.replace("-", " ")
print(f'Исходная строка             : {phone}')
print(f'Замена дефисов на пробел    : {edited_phone}\n')  # +1 234 567 89 10

# удаление дефисов
edited_phone = phone.replace("-", "")
print(f'Исходная строка             : {phone}')
print(f'Удаление дефисов            : {edited_phone}\n')   # +12345678910

# замена только первого дефиса
edited_phone = phone.replace("-", "", 1)
print(f'Исходная строка             : {phone}')
print(f'Замена только первого дефиса: {edited_phone}\n')  # +1234-567-89-10


# Разбиение строки
# split([delimeter[, num]]): разбивает строку на подстроки в зависимости от разделителя
print('\nsplit(): разбивает строку на подстроки в зависимости от разделителя')
text = "Это был огромный, в два обхвата дуб, с обломанными ветвями и с обломанной корой"
# разделение по пробелам
print('\n-----------------------------------------------')
print('разбиение по пробелам')
splitted_text = text.split()
print(text)
print(splitted_text)


# разбиение по запятым
print('\n-----------------------------------------------')
print('разбиение по запятым')
splitted_text = text.split(",")
print(text)
print(splitted_text)


# разбиение по первым пяти пробелам
print('\n-----------------------------------------------')
print('разбиение по первым пяти пробелам')
splitted_text = text.split(" ", 5)
print(text)
print(splitted_text)
print('-----------------------------------------------')


# join(strs): объединяет строки в одну строку, вставляя между ними определенный разделитель
print('\n\njoin(strs): объединяет строки в одну строку, вставляя между ними определенный разделитель')
words = ["Let", "me", "speak", "from", "my", "heart", "in", "English"]

# разделитель - пробел
print('\nразделитель - пробел')
sentence = " ".join(words)
print(sentence)  # Let me speak from my heart in English

# разделитель - вертикальная черта
print('\nразделитель - вертикальная черта')
sentence = " | ".join(words)
print(sentence)  # Let | me | speak | from | my | heart | in | English

word = "hello"
joined_word = "|".join(word)
print(joined_word)      # h|e|l|l|o
