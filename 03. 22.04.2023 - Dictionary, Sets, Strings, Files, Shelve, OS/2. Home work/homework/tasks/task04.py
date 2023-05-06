import shelve

from infrastructure import utils as u
import os

# Task4. Бинарные файлы shelve, модуль os. При помощи модуля os создайте в проекте папку task4, выведите в бинарный 
# файл при помощи модуля shelve список товаров. Каждый элемент списка также список – наименование, цена, 
# признак наличия. В качестве ключа используйте порядковый номер товара в списке. Если файла в папке task4 нет – 
# формируйте список для записи присваиванием и сохраняйте его в файл. Список товаров должен содержать от 10 до 15 
# товаров. Загрузить список из бинарного файла shelve, вычислить сумму цен товаров, имеющихся в наличии и количество 
# наименований товаров, которых нет в наличии. Реализуйте добавление, изменение и удаление товара из файла по команде
# меню задачи (вводить с клавиатуры ничего не требуется, используйте генерацию добавляемого товара, удаление и 
# изменение записи со случайным индексом).


# имя папки
dir_name = 'task04'

# имя файла данных
file_name = 'goods'

# путь к файлу
path_file = os.path.join(dir_name, file_name)


# инициализация списка товаров
# осуществляется загрузка из файла данных, либо при его отсутствии создаётся коллекция и записывается в файл 
def initialization() -> list:
    # создание папки и/или файла с данными
    if not os.path.exists(path_file + '.dat'):
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

        # запись: [наименование, цена, признак наличия]
        goods_list = [
            ['телефон', 273, True], ['чехол', 681, True], ['ноутбук', 442, True], ['чехол', 874, False],
            ['мышь', 697, True], ['монитор', 527, True], ['наушники', 231, False], ['телефон', 430, True],
            ['мышь', 691, False], ['монитор', 1000, True], ['монитор', 967, True], ['телефон', 843, False],
            ['мышь', 702, True], ['ноутбук', 958, False], ['ноутбук', 869, False]
        ]

        save_to_file(path_file, goods_list)

        return goods_list

    return load_from_file(path_file)


# запись данных в файл
def save_to_file(name_file: str, data: list):
    with shelve.open(name_file) as file:
        for i in range(len(data)):
            file[str(i + 1)] = data[i]


# чтение данных из файла
def load_from_file(name_file: str) -> list:
    data = []

    with shelve.open(name_file) as file:
        for key in file:
            data.append(file[key])

    return data


# вывод всех товаров
def show_all(title='Все товары'):
    data = initialization()
    show_table(data, title)


# получить суммарную стоимость товаров в наличии
def get_cost_available(data: list) -> int:
    def predicate_by_available(item: list):
        return item[2]

    data = list(filter(predicate_by_available, data))

    def get_price(item: list):
        return item[1]

    return sum(map(get_price, data))


# получить количество товаров, которых нет в наличии
def get_amount_by_not_available(data: list) -> int:
    def predicate_by_available(item: list):
        return not item[2]

    return len(list(filter(predicate_by_available, data)))


# добавление товара
def add_goods(name: str, price: int, in_stoke: bool) -> None:
    data = initialization()
    data.append([name, price, in_stoke])

    save_to_file(path_file, data)


# изменение товара
def edit_goods(index: int, name: str, price: int, in_stoke: bool) -> None:
    data = initialization()
    data[index] = [name, price, in_stoke]

    save_to_file(path_file, data)


# удаление товара
def remove_goods(index: int):
    data = initialization()
    data.pop(index)

    save_to_file(path_file, data)


# вывод шапки таблицы
def show_header(title: str):
    print(
        u.green_l('╔════════════════════════════════════════════════════════════════╗\n') +
        u.green_l('║ ') + u.purple_l(f'{title:^62}') + u.green_l(' ║\n') +
        u.green_l('╠═════╦════════════════════════════════╦════════════╦════════════╣\n') +
        u.green_l('║ ') + u.purple_l(f'{"N":^3}') +
        u.green_l(' ║ ') + u.purple_l(f'{"Наименование":^30}') +
        u.green_l(' ║ ') + u.purple_l(f'{"Цена":^10}') +
        u.green_l(' ║ ') + u.purple_l(f'{"В наличи":^10}') + u.green_l(' ║\n') +
        u.green_l('╠═════╬════════════════════════════════╬════════════╬════════════╣'))


# вывод строки таблицы
def show_row(n, item: list):
    in_stoke_color = u.cyan_l if item[2] else u.red_l
    in_stoke_value = 'да' if item[2] else 'нет'

    print(
        u.green_l('║ ') + u.black_l(f'{n:3}') +
        u.green_l(' ║ ') + u.cyan_l(f'{item[0]:30}') +
        u.green_l(' ║ ') + u.cyan_l(f'{item[1]:10}') +
        u.green_l(' ║ ') + in_stoke_color(f'{in_stoke_value:10}') + u.green_l(' ║')
    )


# вывод подвала таблицы
def show_footer():
    print(u.green_l('╚═════╩════════════════════════════════╩════════════╩════════════╝'))


# вывод таблицы
def show_table(items: list, title: str):
    show_header(title)

    for i in range(len(items)):
        show_row(i + 1, items[i])

    show_footer()


if __name__ == "__main__":
    from main import main

    main()
