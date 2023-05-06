# Наряду со списками и кортежами Python имеет еще одну встроенную структуру
# данных, которая называется словарь (dictionary). В ряде языков программирования
# есть похожие структуры (словарь в C#, ассоциативный массив в PHP, JS).
#
# Как и список, словарь хранит коллекцию элементов, пары "ключ - значение"
# Каждый элемент в словаре имеет уникальный ключ, с которым ассоциировано некоторое значение.
#
# Определение словаря имеет следующий синтаксис:
# dictionary = { ключ1:значение1, ключ2:значение2, ....}

# В словаре users в качестве ключей используются числа, а в качестве значений - строки.
# В словаре element в качестве ключей используются строки
users = {
    1: "Валентина",
    2: "Алексей",
    3: "Ермолай",
    4: "Полина"
}

elements = {
    "Au": "Золото",
    "Fe": "Железо",
    "H":  "Водород",
    "O":  "Кислород",
    "Al": "Алюминий"
}

# пустой словарь
objects1 = {}
objects2 = dict()

# перебор элементов словаря
# users[key] - значение из пары "ключ -> значение"
for key in users:
    print(f'{key:3} | {users[key]}')
# end for
print()

# еще один пример, имя key для ключа не обязательно
for code in elements:
    print(f'{code:3} | {elements[code]} ')
# end for
print()


# получение кортежей из элементов словаря
for key, value in users.items():
    print(f'{key:3} | {value}')
# end for
print()


# вывод только ключей
for key in users.keys():
    print(key)
# end for
print()

# вывод только значений
for value in users.values():
    print(value)
# end for
print()


# получение, добавление, изменение и удаление элементов словаря
# CRUD - create, read, update, delete
print('\n*** CRUD ***')

# create
# 5 нет в словаре - это добавление элемента
users[5] = "Прасковья"
print(users)

# read
# получаем/читаем элемент с ключом 1 -- read
print(users[1])
print(users.get(1))
print(users.get(100, 'нет пользователя с ид = 100'))

# update
# установка нового значения элемента с ключом 1 - изменение элемента
users[1] = "Дарья"
print(users[1])

# delete
# удаление - операция del
key = 12
if key in users:
    user = users[key]    # только для вывода после удаления
    del users[key]
    print(f'{key}:{user} удален')
else:
    print(f"Элемент с ключом {key} не найден")

# удаление - метод pop(key), возвращает удаляемый элемент или
# выбрасывает исключение
key = 5
if key in users:
    user = users.pop(key)
    print(f'Удален элемент {key}:{user}')
else:
    print(f"Элемент с ключом {key} не найден")

# удаление - метод pop(key, default), возвращает удаляемый элемент или
# значение default
user = users.pop(key, "Нет такого пользователя")
print(f'{key}: {user}')


# очистка словаря
elements.clear()
print(f'\nВ словаре elements элементов: {len(elements)}\n')

# копирование словарей
print('\nКопирование - метод copy()')
users2 = users.copy()
print(users2)

# имзменение словаря
print('\nДобавление в словарь другого словаря - метод update()')
users2.update({12: 'Василий', 23: 'Федор', 123: 'Тамара', 22: 'Юрий'})
print(users2)


# Сложные словари/Комплексные словари
# Кроме простейших объектов типа чисел и строк словари также могут хранить
# и более сложные объекты - те же списки, кортежи или другие словари:
print('\n*** сложные словари ***')

# словарь, содержащий данные о сотрудниках - имена и контакты
employees = {
    "Марина": {
        "телефон": "+38 071 478 74 55",
        "почта": "marina12@gmail.com"
    },
    "Алиса": {
        "телефон": "+38 071 639 04 44",
        "почта": "alice@gmail.com",
        "skype": "alice123"
    },
    "Тимофей": {
        "телефон": "+38 071 123 44 55",
        "почта": "tim111@gmail.com",
        "viber": "tim111"
    }
}

# перебираем сложный словарь
print('\nРаботники:')
for key, value in employees.items():
    print(f'{key:8} - {value}')
# end for


key = "skype"
employee = employees["Алиса"]
if key in employee:
    print(f'\nСкайп Алисы: {employee["skype"]}')
    print(f'Телефон Алисы: {employee["телефон"]}')
else:
    print("skype не найден")
# end if


# перебираем сложный словарь
print('\nРаботники:')
for name, info in employees.items():
    print(f'{name}')
    for messanger, value in info.items():
        print(f'\t{messanger:8}: {value}')
    # end for
    print()
# end for
