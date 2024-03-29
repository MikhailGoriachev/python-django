
# Сортировка списка объектов класса, описывающего товар 
#     o сортировка по наименованию товаров
#     o сортировка по убыванию стоимости
#     o сортировка по возрастанию стоимости
#     o сортировка по убыванию стоимости
#     o сортировка по признаку наличия
#     o сортировка по нескольким полям класса

import app
import utils


# главная функция приложения
def main():

    # начальное формирование списка товаров, каталога и файла данных
    app.generate_list_products(False)

    # меню приложения с функциями обработки задач
    menu_task = {
        '1': ['Вывод списка', app.show_list_goods],
        '2': ['Сортировка по наименованию, функция', app.sort_by_name],
        '3': ['Сортировка по наименованию, лямбда', app.sort_by_name_lambda],
        '4': ['Сортировка по возрастанию стоимости', app.sort_by_cost],
        '5': ['Сортировка по убыванию стоимости', app.sort_by_cost_desc],
        '6': ['Сортировка по признаку наличия, sorted()', app.sorted_by_presence],
        '7': ['Сортировка по нескольким полям класса', app.sort_by_many],
        '0': ['Выход', 0]
    }

    # обработка меню приложения
    utils.do_menu(menu_task, '\t    Меню приложения для демонстрации сортировки списка товаров')
# end main


# запуск главной функции приложения
if __name__ == '__main__':
    main()
#end if
