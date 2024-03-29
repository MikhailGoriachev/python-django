# Множество (set) представляют еще один вид набора элементов.
# Множество содержит только уникальные значения.

# Для определения множества используются фигурные скобки,
# в которых перечисляются элементы
users = {"Тимоша","Боря","Алина", "Тимоша", 2023, False}
print(users)

years = {2022, 1989, 2011, 1942, 2021, 2021, 2021}
print(years)


# Также для определения множества может применяться функция set(),
# в которую передается список или кортеж элементов:

# пример создания множества из списка
users3 = set(["Миша", "Боря", "Федя", "Боря"])
print(users3)

# пример создания множества из кортежа
users3 = set(("Миша", "Боря", "Федя", "Боря", "Юля"))
print(users3)


# Функцию set удобно применять для создания пустого множества:
users3 = set()
print(users3)


# Для получения длины множества применяется встроенная функция len():
print(users)
print(f'Длина множества \033[4musers\033[0m: {len(users)}')

# --------------------------------------------------------------------------

print()

# Добавление элементов
# Для добавления одиночного элемента вызывается метод add():
users.add("Сеня")
print(f'\nДобавление элементов, добавлен 1 элемент: {users}')

# ---------------------------------------------------------------------------

# Удаление элементов
# Для удаления одного элемента вызывается метод remove(), в который передается
# удаляемый элемент. Но следует учитывать, что если такого элемента не окажется
# в множестве, то будет сгенерирована ошибка. Поэтому перед удалением следует
# проверять на наличие элемента с помощью оператора in:
user = "Тимоша"
if user in users:          # поиск в множестве
    users.remove(user)
print(f'\nУдаление элементов, метод remove(): {users}')

# Также для удаления можно использовать метод discard(), который не будет
# генерировать исключения при отсутствии элемента:
# user = "Алина"
users.discard(user)
print(f'\nУдаление элементов, метод discard(): {users}')

# Для удаления всех элементов вызывается метод clear():
users.clear()
print(f'\nУдаление всех элементов, метод clear(): {users}')

# ---------------------------------------------------------------------------

# Перебор множества
# Для перебора элементов можно использовать цикл for:
users = {"Тимоша", "Вася", "Алиса"}

print('\nМножество пользователей')
for user in users:
    print(f'имя пользователя: {user}')
print()

# ---------------------------------------------------------------------------

# !! при присваивании множества не копируются, просто users2 указывает на users
# одно множество и две переменные для доступа к нему :(
users2 = users
print(users2)
users2.add("Вася")
print(users2)
print(users)


# Операции с множествами
# С помощью метода copy() можно скопировать содержимое одного множества в другую переменную:
users = {"Tom","Bob","Alice"}
users3 = users.copy()
print(f'Копия множества users: {users3}')

# Метод union() объединяет два множества и возвращает новое множество:
users = {"Tom","Bob","Alice"}
users2 = {"Sam","Kate", "Bob"}
users3 = users.union(users2)
print(f'Объединение множеств: {users3}')  # {"Bob", "Alice", "Sam", "Kate", "Tom"}

# Пересечение множеств позволяет получить только те элементы, которые есть одновременно
# в обоих множествах. Метод intersection() производит операцию пересечения множеств
# и возвращает новое множество:
users = {"Tom","Bob","Alice"}
users2 = {"Sam","Kate", "Bob", "Tom"}
users3 = users.intersection(users2)
print(f'\n{users}\n{users2}\nПересечение множеств: {users3}')  # {"Bob" "Tom"}

# Вместо метода intersection мы могли бы использовать операцию логического умножения:
users = {"Tom","Bob","Alice"}
users2 = {"Sam","Kate", "Bob", "Tom"}
users3 = users & users2
print(f'\n{users}\n{users2}\nПересечение множеств: {users3}')  # {"Bob" "Tom"}
# В этом случае мы получили бы тот же результат

# Еще одна операция - разность множеств возвращает те элементы, которые есть в
# первом множестве, но отсутствуют во втором. Для получения разности множеств
# можно использовать метод difference или операцию вычитания:
users = {"Tom","Bob","Alice"}
users2 = {"Sam","Kate", "Bob"}
users3 = users.difference(users2)
print(f'\n{users}\n{users2}\nРазность множеств: {users3}')  # {"Tom", "Alice"}
users3 = users - users2
print(f'\n{users}\n{users2}\nРазность множеств: {users3}')  # {"Tom", "Alice"}
print()

# ---------------------------------------------------------------------------

# Отношения между множествами
# Метод issubset позволяет выяснить, является ли текущее множество подмножеством
# (то есть частью) другого множества:
users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
print(f'users: {users}\nsuperusers: {superusers}')

print(f'Является ли users подмножестовм superusers: {users.issubset(superusers)}')   # True
print(f'Является ли superusers подмножестовм users: {superusers.issubset(users)}')   # False

# Метод issuperset, наоборот, возвращает True, если текущее множество является
# надмножеством (то есть содержит) для другого множества:
users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
print(f'Является ли users надмножестовм superusers: {users.issuperset(superusers)}')   # False
print(f'Является ли superusers надмножестовм users: {superusers.issuperset(users)}')   # True
print()

# ---------------------------------------------------------------------------

# frozen set
# Тип frozen set является видом множеств, которое не может быть изменено.
# Для его создания используется функция frozenset:
users = frozenset({"Tom", "Bob", "Alice"})
print(users)

# В функцию frozenset передается набор элементов - список, кортеж, другое множество.
# В такое множество мы не можем добавить новые элементы, как и удалить из него уже имеющиеся.

