# Бинарные файлы в отличие от текстовых хранят информацию в виде набора байт.
# Для работы с ними в Python необходим встроенный модуль pickle.
# Этот модуль предоставляет два метода:
# dump(obj, file): записывает объект obj в бинарный файл file
# load(file)     : считывает данные из бинарного файла в объект
#
# При открытии бинарного файла на чтение или запись также надо учитывать, что
# нам нужно применять режим "b" в дополнение к режиму записи ("w") или чтения ("r").

import pickle

user_file = "user.dat"

name = "Tom"
age = 36

# запись в бинарный файл
with open(user_file, "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
# end with

# чтение из бинарного файла
with open(user_file, "rb") as file:
    name = pickle.load(file)
    age = pickle.load(file)
# end with

print("Имя:", name, "\tВозраст:", age)
print()


# ---------------------------------------------------------------------
# Коллекция данных
users_file = "users.dat"

users = [
    ["Тимофей", 28, True],
    ["Алиса", 23, False],
    ["Jane", 31, False],
    ["Bob", 29, True],
    ["Ольга", 33, False],
    ["Борис", 34, True]
]

# запись коллекции в бинарный файл
with open(users_file, "wb") as file:
    pickle.dump(users, file)
# end with

# чтение коллекции из бинарного файла
with open(users_file, "rb") as file:
    users_from_file = pickle.load(file)
# end with

for user in users_from_file:
    print("Имя:", user[0], "\tВозраст:", user[1], "\tЖенат(замужем):", user[2])

