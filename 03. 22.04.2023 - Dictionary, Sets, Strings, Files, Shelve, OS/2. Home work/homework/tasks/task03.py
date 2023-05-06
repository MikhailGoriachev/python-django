from infrastructure import utils as u
import os
import csv

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


# имя папки
dir_name = 'app_data'

# имя файла данных
file_name = 'countries.csv'

# путь к файлу
path_file = os.path.join(dir_name, file_name)


# инициализация словаря государств
# осуществляется загрузка из файла данных, либо при его отсутствии создаётся коллекция и записывается в файл 
def initialization() -> dict:
    # создание папки и/или файла с данными
    if not os.path.exists(path_file):
        countries = {
            'США': 'Вашингтон',
            'Китай': 'Пекин',
            'Япония': 'Токио',
            'Канада': 'Оттава',
            'Бразилия': 'Бразилиа',
            'Италия': 'Рим',
            'Испания': 'Мадрид',
            'Германия': 'Берлин',
            'Франция': 'Париж',
            'Австралия': 'Канберра',
            'Индия': 'Нью-Дели',
            'Мексика': 'Мехико',
            'Аргентина': 'Буэнос-Айрес',
            'Южная Корея': 'Сеул',
        }
        save_to_file(path_file, countries)

        return countries

    return load_from_file(path_file)


# запись данных в файл
def save_to_file(name_file: str, data: dict):
    with open(name_file, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for d in data:
            writer.writerow([d, data[d]])


# чтение данных из файла
def load_from_file(name_file: str) -> dict:
    data = {}

    with open(name_file, 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data[row[0]] = row[1]

    return data


# вывод всех государств
def show_all(title='Все страны и столицы'):
    data = initialization()
    show_table(data, title)


# столица заданного государства
def get_by_country(country: str) -> str:
    data = initialization()
    return data.get(country, 'Не найдено')


# вывод столицы заданного государства
def show_by_country(country: str):
    capital = get_by_country(country)

    show_header(f'Данные о столице страны "{country}"')
    show_row(1, country, capital)
    show_footer()


# государство, столицей которого является заданный город
def get_by_capital(capital_value: str):
    data = initialization()

    for country, capital in data.items():
        if capital == capital_value:
            return country

    return 'Не найдено'


# вывод государства, столицей которого является заданный город
def show_by_capital(capital: str):
    country = get_by_capital(capital)

    show_header(f'Данные о стране столицей которого является "{capital}"')
    show_row(1, country, capital)
    show_footer()


# добавление государства и его столицы в словарь
def add_country(country: str, capital: str):
    data = initialization()
    data[country] = capital
    save_to_file(path_file, data)


# вывод шапки таблицы
def show_header(title: str):
    print(
        u.green_l('╔═══════════════════════════════════════════════════════════════════════╗\n') +
        u.green_l('║ ') + u.purple_l(f'{title:^69}') + u.green_l(' ║\n') +
        u.green_l('╠═════╦════════════════════════════════╦════════════════════════════════╣\n') +
        u.green_l('║ ') + u.purple_l(f'{"N":^3}') +
        u.green_l(' ║ ') + u.purple_l(f'{"Стана":^30}') +
        u.green_l(' ║ ') + u.purple_l(f'{"Столица":^30}') + u.green_l(' ║\n') +
        u.green_l('╠═════╬════════════════════════════════╬════════════════════════════════╣'))


# вывод строки таблицы
def show_row(n, country, capital):
    country_color = u.cyan_l if country != 'Не найдено' else u.red_l
    capital_color = u.cyan_l if capital != 'Не найдено' else u.red_l

    print(
        u.green_l('║ ') + u.black_l(f'{n:3}') +
        u.green_l(' ║ ') + country_color(f'{country:30}') +
        u.green_l(' ║ ') + capital_color(f'{capital:30}') + u.green_l(' ║')
    )


# вывод подвала таблицы
def show_footer():
    print(u.green_l('╚═════╩════════════════════════════════╩════════════════════════════════╝'))


# вывод таблицы
def show_table(items: dict, title: str):
    show_header(title)

    i = 1
    for key in items:
        show_row(i, key, items[key])
        i += 1

    show_footer()


if __name__ == "__main__":
    from main import main

    main()
