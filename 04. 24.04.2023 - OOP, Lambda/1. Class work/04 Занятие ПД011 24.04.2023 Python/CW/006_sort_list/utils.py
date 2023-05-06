# вспомогательные функции задания
import shelve
import main


# вывод меню из словаря menu_task, выбор в меню и выполнение команд меню
from classes.Product import Product


def do_menu(menu_task, title):
    while True:
        try:
            # вывести меню
            print(title)
            for key, value in menu_task.items():
                print(f'\t \033[34;1m{key}\033[0m. {value[0]}')
            # end for

            # ввести команду меню
            cmd = input('\t    Введите команду: ')

            # специальная команда - выход из цикла
            # обработки меню
            if cmd == '0':
                print()
                break
            # end if

            # выполнить команду меню, если команды нет - сообщить об ошибке
            if cmd in menu_task:
                menu_task[cmd][1]()
            else:
                raise Exception("нет такого пункта меню")
            # end if
        except Exception as e:
            print(f'\n\t\033[31;1mОшибка: {e}\033[0m\n')
        # end try-except
    # end while
# end do_menu


# region Вспомогательные функции для работы сс списком товаров
# возвращает список товаров для обработки
def products_initializer():
    return [
        Product('куртка замшевая', 12000, True),            # 1
        Product('ручка шариковая', 45, True),               # 2
        Product('фотоаппарат импортный', 4500, False),      # 3
        Product('кинокамера отечественная', 8800, True),    # 4
        Product('сапоги резиновые', 230, False),            # 5
        Product('кеды беговые', 70, True),                  # 6
        Product('тарелка фаянсовая', 80, True),             # 7
        Product('кружка алюминиевая', 280, True),           # 8
        Product('полотенце банное', 480, False),            # 9
        Product('мыло душистое', 280, True),                # 10
        Product('мочалка натуральная', 320, True),          # 11
        Product('спирт этиловый', 110, True),               # 12
        Product('средство моющее', 350, False),             # 13
        Product('инсектицид аэрозольный', 280, True)        # 14
    ]
# end products_initializer


# чтение списка из бинарного файла при помощи модуля shelve
def read_list(file_name):
    data = []
    with shelve.open(file_name) as data_file:
        for datum in data_file:
            data.append(data_file[datum])   # data_file[datum] - собственно чтение
        # end for
    # end with
    return data
# end read_list


# запись списка товаров в бинарный файл при помощи модуля shelve
def write_list(file_name, data):
    # запись файла при помощи модуля shelve
    with shelve.open(file_name) as data_file:
        i = 1
        for datum in data:
            # 'data_file[str(i)] =' вместе с присваиванием это и есть запись в файл
            # ключом словаря в данном случае может быть строка, не может быть int
            data_file[str(i)] = datum
            i += 1
        # end for
    # end with
# end write_list


# выводим список товаров в табличном формате
def show_list_goods(title, data):
    # вывод заголовка таблицы товаров
    # обращение к статическому атрибуту класса - Goods.header
    print(f'\t\t\033[30;1m{title}\n{Product.header}')

    # вывод основной части таблицы товаров
    i = 1
    for goods in data:
        print(f'{goods.to_table_row(i)}')
        i += 1

    # вывод подвала таблицы товаров - обращение к статическому атрибуту класса Goods
    print(f'{Product.footer}\033[0m\n')
# end show_list_goods


# возвращает сумму цен товаров, имеющихся в наличии
def sum_presents(list_goods):
    summa = 0
    for goods in list_goods:
        if goods.present:
            summa += goods.price
    # end for

    return summa
# end sum_presents
# endregion

# запуск главной функции приложения
if __name__ == '__main__':
    main.main()
# end if
