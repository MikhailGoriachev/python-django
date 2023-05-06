import random

import utils


# Task2. Обработка списков. Для списков, заполненных случайными числами в диапазоне значений от –20 до 20, выводите 
# сформированные списки до и после обработки по заданию.
#   — Сформируйте список list_c. Увеличить все нечетные числа, содержащиеся в списке, на исходное значение последнего 
#     нечетного числа. Если нечетные числа в списке отсутствуют, то оставить список без изменений. Вывести упорядоченную 
#     по убыванию копию списка
#   — Сформируйте список list_c. Возвести в квадрат все его локальные минимумы (то есть числа, меньшие своих соседей)
#   — Сформируйте список list_c. Удалить из списка все одинаковые элементы, оставив их первые вхождения
#   — Сформируйте список list_c. Вставить элемент с нулевым значением перед минимальным и после максимального 
#     элемента списка

# создание списка
def create_list(n=10, min_val=-20, max_val=20):
    items = []
    for i in range(n):
        items.append(random.randint(min_val, max_val))
    return items


# увеличить все нечетные числа, содержащиеся в списке, на исходное значение последнего 
# по убыванию копию списка нечетного числа. Если нечетные числа в списке отсутствуют, то оставить список без изменений. 
# Вывести упорядоченную по убыванию копию списка
def proc01():
    items = create_list()

    utils.show_table(items, "Обработка 1. Сгенерированный список")

    # упорядочивание по убыванию
    result = sorted(items)

    # значение последнего нечётного элемента
    last_odd = get_last_odd(result)

    # если нет нечётных элементов
    if last_odd is None:
        utils.show_table(items, "Обработка 1. В списке нет нечётных элементов")
        utils.show_table(items, "Обработка 1. Отсортированный список по убыванию")
        return

    # изменение копии коллекции
    increase_to_odd_elems(items, last_odd)

    # сортировка по убыванию
    result = sorted(items)
    result.reverse()

    utils.show_table(items, f"Обработка 1. Все нечётные числа увеличены на значение: {last_odd}")
    utils.show_table(result, "Обработка 1. Отсортированный список по убыванию")


# получить первый нечётный элемент
# если такого нет, то возвращается None
def get_last_odd(items: list):
    first_odd = None

    for i in range(len(items)):
        if (items[i] & 1) == 1:
            first_odd = items[i]
            break

    return first_odd


# увеличить все нечетные числа, содержащиеся в списке на заданное значение
def increase_to_odd_elems(items: list, value):
    for i in range(len(items)):
        if (items[i] & 1) == 1:
            items[i] += value


# возвести в квадрат все локальные минимумы (то есть числа, меньшие своих соседей)
def proc02():
    items = create_list()

    utils.show_table(items, "Обработка 2. Сгенерированный список")

    local_min_to_square(items)

    utils.show_table(items, "Обработка 2. Локальные минимумы возведены в квадрат")


# возведение локальных минимумов в квадрат
def local_min_to_square(items: list):
    for i in range(1, len(items) - 1):
        prev_val = items[i - 1]
        cur_val = items[i]
        next_val = items[i + 1]

        if prev_val > cur_val and next_val > cur_val:
            items[i] **= 2


# удалить из списка все одинаковые элементы, оставив их первые вхождения
def proc03():
    items = create_list()

    utils.show_table(items, "Обработка 3. Сгенерированный список")

    items.reverse()

    i = 0
    while i < len(items):
        if (items.count(items[i])) > 1:
            items.pop(i)
        else:
            i += 1

    items.reverse()

    utils.show_table(items, "Обработка 3. Удалены дубликаты, оставлены первые вхождения")


# вставить элемент с нулевым значением перед минимальным и после максимального элемента списка
def proc04():
    items = create_list()

    utils.show_table(items, "Обработка 4. Сгенерированный список")

    min_i = items.index(min(items))
    max_i = items.index(max(items))

    insert_val = 0

    items.insert(min_i, insert_val)
    items.insert(max_i + 1, insert_val)

    utils.show_table(items, "Обработка 3. Вставлены нулевые элементы перед минимальным и после максимального")


if __name__ == "__main__":
    from main import main

    main()
