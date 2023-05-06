import infrastructure.utils as u


# Специальность доктора
class Speciality:

    def __init__(self, _id: int, name: str):
        self.__id = _id
        self.__name = name

    # id
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int):
        if not value >= 0:
            raise ValueError('Поле id должно быть больше либо равно 0')
        self.__id = value

    # наименование
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError('Поле наименования должно быть заполнено')
        self.__name = value

    # формирование строки таблицы
    def to_table_row(self) -> str:
        return u.green('║ ') + u.black_l(f'{self.__id:3}') + \
            u.green(' ║ ') + u.cyan(f'{self.__name:20}') + u.green(' ║\n')

    # вывод шапки таблицы
    @staticmethod
    def show_header(title: str):
        print(
            u.green('╔════════════════════════════╗\n') +
            u.green('║ ') + u.purple(f'{title:^26}') + u.green(' ║\n') +
            u.green('╠═════╦══════════════════════╣\n') +
            u.green('║ ') + u.purple(f'{"ID":^3}') +
            u.green(' ║ ') + u.purple(f'{"Наименование":^20}') + u.green(' ║\n') +
            u.green('╠═════╬══════════════════════╣'))

    # вывод подвала таблицы
    @staticmethod
    def show_footer():
        print(u.green(
            '╚═════╩══════════════════════╝'))

    # вывод таблицы
    @staticmethod
    def show_table(items: list, title: str = 'Все специальности'):
        Speciality.show_header(title)

        rows = ''
        for item in items:
            rows += item.to_table_row()
        print(rows, end='')

        Speciality.show_footer()
