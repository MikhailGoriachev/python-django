import datetime
import infrastructure.utils as u

from entities.Person import Person


class Patient:

    def __init__(self, _id: int, person: Person, born_date: datetime, address: str, passport: str):
        self.__id = _id
        self.__person = person
        self.__born_date = born_date
        self.__address = address
        self.__passport = passport

    # id
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int):
        if not value >= 0:
            raise ValueError('Поле id должно быть больше либо равно 0')
        self.__id = value

    # персона
    @property
    def person(self) -> Person:
        return self.__person

    @person.setter
    def person(self, value: Person):
        self.__person = value

    # дата рождения
    @property
    def born_date(self) -> datetime:
        return self.__born_date

    @born_date.setter
    def born_date(self, value: datetime):
        self.__born_date = value

    # адрес
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value: str):
        if not value:
            raise ValueError('Поле адреса должно быть заполнено')
        self.__address = value

    # паспорт
    @property
    def passport(self) -> str:
        return self.__passport

    @passport.setter
    def passport(self, value: str):
        if not value:
            raise ValueError('Поле паспорта должно быть заполнено')
        self.__passport = value

    # формирование строки таблицы
    def to_table_row(self) -> str:
        return u.green('║ ') + u.black_l(f'{self.__id:3}') + \
            u.green(' ║ ') + u.cyan(f'{self.person.surname:20}') + \
            u.green(' ║ ') + u.cyan(f'{self.person.name:20}') + \
            u.green(' ║ ') + u.cyan(f'{self.person.patronymic:20}') + \
            u.green(' ║ ') + u.cyan(f'{self.__passport:10}') + \
            u.green(' ║ ') + u.cyan(f'{u.get_local_format_date(self.__born_date):15}') + \
            u.green(' ║ ') + u.cyan(f'{self.__address:35}') + u.green(' ║\n')

    # вывод шапки таблицы
    @staticmethod
    def show_header(title: str):
        print(
            u.green(
                '╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\n') +
            u.green('║ ') + u.purple(f'{title:^141}') + u.green(' ║\n') +
            u.green(
                '╠═════╦══════════════════════╦══════════════════════╦══════════════════════╦════════════╦═════════════════╦═════════════════════════════════════╣\n') +
            u.green('║ ') + u.purple(f'{"ID":^3}') +
            u.green(' ║ ') + u.purple(f'{"Фамилия":^20}') +
            u.green(' ║ ') + u.purple(f'{"Имя":^20}') +
            u.green(' ║ ') + u.purple(f'{"Отчество":^20}') +
            u.green(' ║ ') + u.purple(f'{"Паспорт":^10}') +
            u.green(' ║ ') + u.purple(f'{"Дата рождения":^15}') +
            u.green(' ║ ') + u.purple(f'{"Адрес":^35}') + u.green(' ║\n') +
            u.green(
                '╠═════╬══════════════════════╬══════════════════════╬══════════════════════╬════════════╬═════════════════╬═════════════════════════════════════╣'))

    # вывод подвала таблицы
    @staticmethod
    def show_footer():
        print(u.green(
            '╚═════╩══════════════════════╩══════════════════════╩══════════════════════╩════════════╩═════════════════╩═════════════════════════════════════╝'))

    # вывод таблицы
    @staticmethod
    def show_table(items: list, title: str = 'Все пациенты'):
        Patient.show_header(title)

        rows = ''
        for item in items:
            rows += item.to_table_row()
        print(rows, end='')

        Patient.show_footer()
