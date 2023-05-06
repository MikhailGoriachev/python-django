import random

import tasks.task01 as task01
import tasks.task02 as task02
import tasks.task03 as task03
import tasks.task04 as task04
import infrastructure.utils as u


# Task1. Обработка множеств. Разработайте функцию, в которой используются два множества из случайных целых чисел. 
# Функция должна обеспечивать:
#   — Формирование множеств – используйте операцию добавления в множество, длина каждого множества определяется 
#     генератором случайных чисел (от 5и до 23х элементов), диапазон значений элементов: -20, 20;
#   — Вычисление пересечения множеств;
#   — Вычисление разности множеств;
#   — Вычисление объединения множеств;
#   — Удаление всех отрицательных элементов из множества с меньшим количеством элементов 
def point01():
    # 1. Формирование множеств
    print(u.green_l('\n\n\n1. Формирование множеств'))

    task01.set_values_a = task01.create_set()
    task01.set_values_b = task01.create_set()

    task01.show_set('Множество A', task01.set_values_a)
    task01.show_set('Множество B', task01.set_values_b)

    # 2. Вычисление пересечения множеств
    print(u.green_l('2. Вычисление пересечения множеств'))

    task01.show_set('Множество A', task01.set_values_a)
    task01.show_set('Множество B', task01.set_values_b)

    intersection = task01.get_intersection(task01.set_values_a, task01.set_values_b)

    task01.show_set('Пересечение', intersection)

    # 3. Вычисление разности множеств
    print(u.green_l('3. Вычисление разности множеств'))

    task01.show_set('Множество A', task01.set_values_a)
    task01.show_set('Множество B', task01.set_values_b)

    different = task01.get_different(task01.set_values_a, task01.set_values_b)

    task01.show_set('Разность', different)

    # 4. Вычисление объединения множеств
    print(u.green_l('4. Вычисление объединения множеств'))

    task01.show_set('Множество A', task01.set_values_a)
    task01.show_set('Множество B', task01.set_values_b)

    join = task01.get_join(task01.set_values_a, task01.set_values_b)

    task01.show_set('Объединение', join)

    # 5. Удаление всех отрицательных элементов из множества с меньшим количеством элементов
    print(u.green_l('5. Удаление всех отрицательных элементов из множества с меньшим количеством элементов'))

    task01.show_set('Множество A', task01.set_values_a)
    task01.show_set('Множество B', task01.set_values_b)

    set_and_title = (task01.set_values_a, 'A') \
        if len(task01.set_values_a) > len(task01.set_values_b) \
        else (task01.set_values_b, 'B')

    task01.show_set(f'Множество с наименьшим количеством элементов {set_and_title[1]}', set_and_title[0])

    task01.remove_negative(set_and_title[0])

    task01.show_set('Множество после удаления', set_and_title[0])


# Task2. Обработка строк, текстовых файлов. Для файла text.txt, приведенного в папке задания реализуйте обработки 
# (файл скопируйте в Ваш проект при создании проекта):
#   — Перевести текст из исходного файла в нижний регистр, сохранить в файле lowers.txt
#   — В файле lowers.txt подсчитать количество строк, слов, определить максимальную длину слова и список слов 
#     максимальной длины, минимальную длину слова и список слов минимальной длины, сохраните списки слов в файлах 
#     longest.txt и shortest.txt соответственно для слов максимальной и минимальной длины
#   — Сформируйте словарь из слов файла lowers.txt – ключом является слово, значением – количество вхождений этого слова 
#     в текст. Сохраните этот словарь в формате CSV, имя файла words.csv
def point02():
    # 1. Перевести текст из исходного файла в нижний регистр, сохранить в файле lowers.txt
    task02.proc01()

    # 2. Статистика слов
    task02.proc02()

    # 3. Частотный словарь
    task02.proc03()


# Task3. Обработка словарей, файлов в формате CSV. Разработайте словарь с названиями ряда государств и их столицами. 
# Реализуйте операции:
#   — вывод столицы заданного государства;
#   — вывод государства, столицей которого является заданный город;
#   — запись словаря в файл формата CSV, имя файл – countries.csv, имя жестко задано, реализовывать выбор из файловой 
#     системы не надо
#   — чтение словаря из файла формата CSV, имя файла – countries.csv, имя жестко задано, реализовывать выбор из файловой
#     системы не надо
#   — добавление государства и его столицы в словарь
# Если заданного государства или города в словаре нет, на экран должно выводиться соответствующее сообщение. 
def point03():
    # 1. Все государства
    print(u.green_l('\n\n\n1. Все государства'))
    task03.show_all()

    data = task03.initialization()

    # 2. Столица заданного государства
    print(u.green_l('\n2. Столица заданного государства'))
    country = random.choice(list(data.keys()))
    task03.show_by_country(country)

    country = 'Нортумбрия'
    task03.show_by_country(country)

    # 3. Государство с заданной столицей
    print(u.green_l('\n3. Государство с заданной столицей'))

    capital = data[random.choice(list(data.keys()))]
    task03.show_by_capital(capital)

    capital = 'Бамборо Эофорвик'
    task03.show_by_capital(capital)

    # 4. Добавление государства и его столицы в словарь
    print(u.green_l('\n4. Добавление государства и его столицы в словарь'))

    print(u.cyan_l('\tВведите название государства: '), end='')
    country = input()
    print(u.cyan_l('\tВведите название столицы: '), end='')
    capital = input()

    task03.add_country(country, capital)

    task03.show_all(f'Добавлена страна "{country}" со столицей "{capital}"')


# Task4. Бинарные файлы shelve, модуль os. При помощи модуля os создайте в проекте папку task4, выведите в бинарный 
# файл при помощи модуля shelve список товаров. Каждый элемент списка также список – наименование, цена, 
# признак наличия. В качестве ключа используйте порядковый номер товара в списке. Если файла в папке task4 нет – 
# формируйте список для записи присваиванием и сохраняйте его в файл. Список товаров должен содержать от 10 до 15 
# товаров. Загрузить список из бинарного файла shelve, вычислить сумму цен товаров, имеющихся в наличии и количество 
# наименований товаров, которых нет в наличии. Реализуйте добавление, изменение и удаление товара из файла по команде
# меню задачи (вводить с клавиатуры ничего не требуется, используйте генерацию добавляемого товара, удаление и 
# изменение записи со случайным индексом).
def point04():
    # 1. Все товары
    print(u.green_l('\n\n\n1. Все товары'))
    task04.show_all()

    data = task04.initialization()

    cost_available = task04.get_cost_available(data)
    amount_not_available = task04.get_amount_by_not_available(data)

    print(
        u.green_l(f'\nСуммарная стоимость товаров в наличии    : {u.cyan_l(cost_available)}\n') +
        u.green_l(f'Количество товаров, которых нет в наличии: {u.cyan_l(amount_not_available)}')
    )

    # 2. Добавление товара
    task04.add_goods('Кеды Adidas', random.randint(1, 5) * 1000, random.choice([True, False]))
    print(u.green_l('\n2. Добавление товара'))
    task04.show_all('Товар добавлен')

    # 3. Изменение товара
    task04.add_goods('Кеды Nike', random.randint(1, 5) * 1000, random.choice([True, False]))
    print(u.green_l('\n3. Последний товар изменён'))
    task04.show_all('Товар изменён')

    # 3. Удаление товара
    index = random.randrange(0, len(task04.initialization()))
    print(u.green_l(f'\n4. Удаление товара с порядковым номером {index + 1}'))
    task04.show_all('До удаления')

    task04.remove_goods(index)

    task04.show_all('После удаления')


if __name__ == "__main__":
    from main import main

    main()
