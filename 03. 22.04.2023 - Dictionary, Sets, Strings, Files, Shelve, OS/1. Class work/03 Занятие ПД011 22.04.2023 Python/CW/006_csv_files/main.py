# Файлы в формате CSV

# Одним из распространенных файловых форматов, которые хранят в удобном виде
# информацию, является формат csv. Каждая строка в файле csv представляет
# отдельную запись или строку, которая состоит из отдельных столбцов, разделенных
# запятыми.
#
# Собственно поэтому формат и называется Comma Separated Values. Но хотя формат
# csv - это формат текстовых файлов, Python для упрощения работы с ним предоставляет
# специальный встроенный модуль csv

import csv

# имя файла данных
FILENAME = "users.csv"

users = [
    ["Тимофей", 28],
    ["Алиса", 23],
    ["Jane", 31],
    ["Bob", 29],
    ["Ольга", 33],
    ["Борис", 34]
]

# newline="" - пустая строка позволяет корректно записывать и считывать строки из
# файла вне зависимости от операционной системы.
print('\nЗапись данных в файл')
with open(FILENAME, "w", encoding='UTF-8', newline="") as file:
    # объект для записи в файл
    writer = csv.writer(file)

    # собственно запись в файл всего списка данных writerows()
    writer.writerows(users)


print('\nДозапись данных в файл')
with open(FILENAME, "a", encoding='UTF-8', newline="") as file:
    # объект для записи в файл
    writer = csv.writer(file)

    # собственно запись в файл writerow()
    writer.writerow(["Сергей", 31])
    writer.writerow(["Валентина", 28])
# end with

# Чтение данных из файла
print('\nЧтение данных из файла')
with open(FILENAME, "r", encoding='UTF-8', newline="") as file:
    # объект для чтения из файла
    reader = csv.reader(file)

    # собственно чтение данных в список
    users = list()
    for row in reader:
        users.append([row[0], row[1]])
        # print(row[0], " - ", row[1])
# end with

# вывод списка
for user in users:
    print(user)
print()


# ----------------------------------------------------------

# Работа со словарями
# В разобранных примерах каждая запись или строка представляла собой отдельный
# список, например, ["Sam", 31]. Но кроме того, модуль csv имеет специальные
# дополнительные возможности для работы со словарями.
# В частности, функция csv.DictWriter() возвращает объект writer, который позволяет
# записывать в файл.
# А функция csv.DictReader() возвращает объект reader для чтения из файла.
customers = [
    {"name": "Тимофей", "amount": 28000, "goods": "зонтик автоматический"},
    {"name": "Алина", "amount": 23000, "goods": "куртка замшевая"},
    {"name": "Борис", "amount": 34000, "goods": "ручка шариковая"},
    {"name": "Марина", "amount": 22000, "goods": "сапоги резиновые"},
    {"name": "Лидия", "amount": 55000, "goods": "кинокамера импортная"}
]

file_name = 'customers.csv'

with open(file_name, "w", newline="", encoding='UTF-8') as file:
    columns = ["name", "amount", "goods"]
    writer = csv.DictWriter(file, fieldnames=columns)
    # writer = csv.DictWriter(file, fieldnames=["name", "amount", "goods"])

    # запись заголовка - строка с именами ключей
    writer.writeheader()

    # запись всей коллекции customers в файл - writerows()
    writer.writerows(customers)

    # запись одной строки  - writerow()
    customer = {"name": "Sam", "amount": 41000, "goods":"планшет китайский"}
    writer.writerow(customer)

# чтение словаря из файла
with open(file_name, "r", newline="", encoding='UTF=8') as file:
    reader = csv.DictReader(file)

    # чтение и вывод данных, не обязательно выводить все поля
    # сохранение прочитанных данных в коллекции
    info = []
    for row in reader:
        print(f'{row["name"]} - {row["amount"]} - {row["goods"]}')
        info.append([row["name"], row["amount"], row["goods"]])
# end with


# обработка данных из коллекции
print()
for datum in info:
    print(datum)
