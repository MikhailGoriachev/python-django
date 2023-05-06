from infrastructure import utils as u


class Animal:
    def __init__(self,
                 name: str = 'нет данных',
                 weight: float = 0.1,
                 age: int = 1,
                 color: str = 'нет данных',
                 owner: str = 'нет данных') -> None:
        self.__name = name
        self.__weight = weight
        self.__age = age
        self.__color = color
        self.__owner = owner

    # клички животного,
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not len(value) > 0:
            raise ValueError('Кличка животного должна быть заполнена')
        self.__name = value

    # веса (в кг),
    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, value: float):
        if not value > 0:
            raise ValueError('Вес животного должен быть больше 0')
        self.__weight = value

    # возраста (в полных годах),
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value: int):
        if not value >= 0:
            raise ValueError('Возраст животного должен быть больше или равен 0')
        self.__age = value

    # цвета (масть) животного,
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, value: str):
        if not len(value) > 0:
            raise ValueError('Цвет животного должен быть заполнен')
        self.__color = value

    # фамилии и инициалов владельца (Иванов И.И., …).
    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, value: str):
        if not len(value) > 0:
            raise ValueError('Фамилия и инициалы владельца животного должны быть заполнены')
        self.__owner = value

    # строковое представление объекта для таблицы
    def __str__(self, n: int = 1) -> str:
        return u.green_l('║ ') + u.black_l(f'{n:3}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.__name:20}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.__weight:10}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.__age:10}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.__color:20}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.__owner:20}') + u.green_l(' ║\n')

    # вывод шапки таблицы
    @staticmethod
    def show_header(title: str):
        print(
            u.green_l(
                '╔════════════════════════════════════════════════════════════════════════════════════════════════════╗\n') +
            u.green_l('║ ') + u.purple_l(f'{title:^98}') + u.green_l(' ║\n') +
            u.green_l(
                '╠═════╦══════════════════════╦════════════╦════════════╦══════════════════════╦══════════════════════╣\n') +
            u.green_l('║ ') + u.purple_l(f'{"N":^3}') +
            u.green_l(' ║ ') + u.purple_l(f'{"Кличка":^20}') +
            u.green_l(' ║ ') + u.purple_l(f'{"Вес":^10}') +
            u.green_l(' ║ ') + u.purple_l(f'{"Возраст":^10}') +
            u.green_l(' ║ ') + u.purple_l(f'{"Цвет":^20}') +
            u.green_l(' ║ ') + u.purple_l(f'{"Владелец":^20}') + u.green_l(' ║\n') +
            u.green_l(
                '╠═════╬══════════════════════╬════════════╬════════════╬══════════════════════╬══════════════════════╣'))

    # вывод подвала таблицы
    @staticmethod
    def show_footer():
        print(u.green_l(
            '╚═════╩══════════════════════╩════════════╩════════════╩══════════════════════╩══════════════════════╝'))

    # вывод таблицы
    @staticmethod
    def show_table(items: list, title: str):
        Animal.show_header(title)

        rows = ''
        for i in range(len(items)):
            rows += items[i].__str__(i + 1)
        print(rows, end='')

        Animal.show_footer()
