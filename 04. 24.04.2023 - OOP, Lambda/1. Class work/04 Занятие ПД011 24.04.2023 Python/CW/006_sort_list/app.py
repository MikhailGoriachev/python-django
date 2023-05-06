import os

import main
import utils

# region классы, бинарный файл, сортировки списка
task3_dir = 'task3'        # имя папки для размещения файла данных по заданию
task3_file_name = 'goods'  # имя файла для хранения списка в бинарном файле
list_products = []            # список товаров


# Чтение из файла или формирование списка товаров, каждый элемент списка
# объект класса Goods со свойствами
#     o наименование
#     o цена
#     o признак наличия
# show: признак вывода списка товаров в консоль
# Если файла данных нет - он создается, если файл
# данных есть - читаем список товаров из него
def generate_list_products(show=True):
    global list_products

    # если файл данных не найден - создать папку (если ее еще нет),
    # сгенерировать список, сохранить список в файле данных
    # иначе - загрузить список товаров из файла данных
    path_file = task3_dir + '/' + task3_file_name

    if not os.path.exists(path_file):
        list_products = utils.products_initializer()      # сгенерировать список товаров
        if not os.path.exists(task3_dir):           # создать папку для файла данных
            os.mkdir(task3_dir)
        # end if
        utils.write_list(path_file, list_products)     # записать файл данных
    # end if
    list_products = utils.read_list(path_file)     # чтение файла данных

    # выведем сформированный список товаров, если установлен параметра show
    if show:
        utils.show_list_goods('\n\tСформирован список товаров для обработки', list_products)
    # end if
# end generate_list_products


# вывод списка товаров в консоль
def show_list_goods():
    utils.show_list_goods('\n\tСписок товаров для обработки', list_products)
# end show_list_goods


# сортировка по наименованию товаров
def sort_by_name():
    # функция, используемая для сортировки, возвращает поле для сортировки
    def get_name(datum): return datum.name

    # для сортировки списка - вызывать метод sort()
    list_products.sort(key=get_name)
    utils.show_list_goods('\n\Товары отсортированы по наименованию', list_products)
# end sort_by_name


# сортировка по наименованию товаров - использование лямбда-выражений
# https://webdevblog.ru/kak-ispolzovat-v-python-lyambda-funkcii/
def sort_by_name_lambda():
    # лямбда-выражение - анонимная функиця
    # lambda параметр: выражение
    list_products.sort(key=lambda datum: datum.name)
    utils.show_list_goods('\n\tТовары отсортированы по наименованию', list_products)
# end sort_by_name_lambda


# Сортировка по возрастанию стоимости
def sort_by_cost():
    list_products.sort(key=lambda datum: datum.price)
    utils.show_list_goods('\n\tТовары отсортированы по возрастанию стоимости', list_products)
# end sort_by_cost


# Сортировка по убыванию стоимости
def sort_by_cost_desc():
    list_products.sort(key=lambda datum: datum.price, reverse=True)
    utils.show_list_goods('\n\tТовары отсортированы по убыванию стоимости', list_products)
# end sort_by_cost_desc


# сортировка без изменения исходного списка
def sorted_by_presence():
    # sort() меняет коллекцию
    # list_goods.sort(key=lambda datum: datum.present)
    # utils.show_list_goods('\n\tТовары по признаку наличия/отсутствия товара', list_goods)
    # sorted() возвращает отсортированный список, не меняя исходный
    list1 = sorted(list_products, key=lambda datum:datum.present)
    utils.show_list_goods('\n\tТовары по признаку наличия/отсутствия товара', list1)
    utils.show_list_goods('\n\tИсходная коллекция товара не изменилась:', list_products)
# end sorted_by_presence


# сортировка по нескольким полям класса - по признаку наличия, и по цене
def sort_by_many():
    list_products.sort(key=lambda datum: (datum.present, datum.price))
    utils.show_list_goods('\n\tТовар упорядоченный по признаку наличия, внутри признака - по цене:', list_products)
# end sort_by_many


# запуск главной функции приложения
if __name__ == '__main__':
    main.main()
# end if
