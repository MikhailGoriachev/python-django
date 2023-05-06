# Класс Product со свойствами
#     o наименование
#     o цена
#     o признак наличия
class Product:
    # статический атрибут класса - заголовок таблицы
    header = \
        '\t┌─────┬──────────────────────────┬────────────┬───────────────┐\n'\
        '\t│  №  │ Наименование             │ Стоимость  │ Наличие       │\n'\
        '\t│ п/п │              товара      │ ед. товара │        товара │\n'\
        '\t├─────┼──────────────────────────┼────────────┼───────────────┤'

    # статический атрибут класса - подвал таблицы
    footer = \
        '\t└─────┴──────────────────────────┴────────────┴───────────────┘'

    # конструктор класса
    def __init__(self, name, price, present):
        self.__name = name         # наименование товара
        self.__price = price       # цена товара
        self.present = present     # признак наличия товара, открытое поле, т.к. логический тип
    # end __init__

    # region свойства класса
    @property     # наименование товара - геттер
    def name(self):
        return self.__name
    # end name

    @name.setter  # наименование товара - сеттер
    def name(self, value):
        if len(value) == 0:
            raise AttributeError('Goods: пустая строка в качестве имени товара')
        # if
        self.__name = value
    # end name

    @property  # цена товара - геттер
    def price(self):
        return self.__price
        # end price

    @price.setter  # цена товара - сеттер
    def price(self, value):
        if value < 0:
            raise AttributeError('Goods: отрицательнаая цена товара')
        # if
        self.__price = value
    # end price
    # endregion

    # вспомогательный метод для строкового представления признака наличия товара
    def present_str(self):
        return 'в наличии' if self.present else 'отсутствует'
    # end present_str

    # строковое представление объекта
    def __str__(self):
        # сформировать и вернуть строковое представление товара
        return f'Товар. Наименование "{self.__name}", цена {self.__price}.00, товар \033[1m{self.present_str()}\033[0m'
    # end __str__

    # вывод объекта в виде строки таблицы
    def to_table_row(self, i):
        # сформировать и вернуть строку таблицы
        return f'\t│ {i:3} │ {self.__name:24} │ {self.__price:7}.00 │  {self.present_str():11}  │'
    # end to_table_row
# end class Product

