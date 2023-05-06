import infrastructure.utils as u


class Person:

    def __init__(self, _id: int, surname: str, name: str, patronymic: str):
        self.__id = _id
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic

    # id
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int):
        if not value >= 0:
            raise ValueError('Поле id должно быть больше либо равно 0')
        self.__id = value

    # фамилия
    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, value: str):
        if not value:
            raise ValueError('Поле фамилии должно быть заполнено')
        self.__surname = value

    # имя
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError('Поле имени должно быть заполнено')
        self.__name = value

    # отчество
    @property
    def patronymic(self) -> str:
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value: str):
        if not value:
            raise ValueError('Поле отчество должно быть заполнено')
        self.__patronymic = value

    # формирование строки таблицы
    def to_table_row(self) -> str:
        return u.green('║ ') + u.black_l(f'{self.__id:3}') + \
            u.green(' ║ ') + u.cyan(f'{self.__surname:20}') + \
            u.green(' ║ ') + u.cyan(f'{self.__name:20}') + \
            u.green(' ║ ') + u.cyan(f'{self.__patronymic:20}') + u.green(' ║\n')

    # вывод шапки таблицы
    @staticmethod
    def show_header(title: str):
        print(
            u.green('╔══════════════════════════════════════════════════════════════════════════╗\n') +
            u.green('║ ') + u.purple(f'{title:^72}') + u.green(' ║\n') +
            u.green('╠═════╦══════════════════════╦══════════════════════╦══════════════════════╣\n') +
            u.green('║ ') + u.purple(f'{"ID":^3}') +
            u.green(' ║ ') + u.purple(f'{"Фамилия":^20}') +
            u.green(' ║ ') + u.purple(f'{"Имя":^20}') +
            u.green(' ║ ') + u.purple(f'{"Отчество":^20}') + u.green(' ║\n') +
            u.green('╠═════╬══════════════════════╬══════════════════════╬══════════════════════╣'))

    # вывод подвала таблицы
    @staticmethod
    def show_footer():
        print(u.green(
            '╚═════╩══════════════════════╩══════════════════════╩══════════════════════╝'))

    # вывод таблицы
    @staticmethod
    def show_table(items: list, title: str = 'Все персоны'):
        Person.show_header(title)

        rows = ''
        for item in items:
            rows += item.to_table_row()
        print(rows, end='')

        Person.show_footer()
