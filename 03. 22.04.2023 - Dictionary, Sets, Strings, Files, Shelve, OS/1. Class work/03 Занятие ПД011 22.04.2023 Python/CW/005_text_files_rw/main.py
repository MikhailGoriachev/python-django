# Запись в текстовый файл
import random

file_name = 'text.txt'

a = random.randint(-100, 100)

# не обязательно, но можно задавать кодировку файла encoding='utf-8'
with open(file_name, "w", encoding='utf-8') as hello_file:
    # строка для записи
    s = f"Hello, world.\nЧисло = {a}\n"

    # 1й способ записи в файл
    hello_file.write(s)

    # 2й способ записи в файл
    print(s, file=hello_file)

    print('-------------------------------\n', file=hello_file)

# Чтение текстового файла
# Для чтения файла он открывается с режимом r (Read), и затем мы можем считать
# его содержимое различными методами:
#
# readline() : считывает одну строку из файла
# read()     : считывает все содержимое файла в одну строку
# readlines(): считывает все строки файла в список

# Считаем и выведем в консоль файл построчно, с явным использованием readline()
with open(file_name, "r", encoding='utf-8') as file:
    # !! чтение 1й строки вне цикла - т.к. while :(
    line = file.readline()

    while line:
        print(line, end="")
        line = file.readline()
# end with
print()

# Считаем и выведем в консоль файл построчно, без явного использования readline()
with open(file_name, "r", encoding='utf-8') as file:
    for line in file:
        print(line, end="")
# end with
print()

# Считаем файл одной операцией read()
with open(file_name, "r", encoding='utf-8') as file:
    lines = file.read()

    for line in lines:
        print(line, end="")
# end with
print()

# Считаем файл одной операцией readlines()
with open(file_name, "r", encoding='utf-8') as file:
    lines = file.readlines()

    for line in lines:
        print(line, end="")
# end with
print()