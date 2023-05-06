from entities.Person import Person
from entities.Speciality import Speciality

import infrastructure.utils as u


class Doctor:

    def __init__(self, _id: int,
                 person: Person,
                 speciality: Speciality,
                 price: int,
                 percent: float):
        self.__id = _id
        self.__person = person
        self.__speciality = speciality

        # цена приёма
        self.__price = price

        # процент отчислений врачу
        self.__percent = percent

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

    # специальность
    @property
    def speciality(self) -> Speciality:
        return self.__speciality

    @speciality.setter
    def speciality(self, value: Speciality):
        self.__speciality = value

    # цена приёма
    @property
    def price(self) -> int:
        return self.__price

    @price.setter
    def price(self, value: int):
        if not value >= 0:
            raise ValueError('Поле цены приёма должно быть больше или равно 0')
        self.__price = value

    # процент отчислений врачу
    @property
    def percent(self) -> float:
        return self.__percent

    @percent.setter
    def percent(self, value: float):
        if not value >= 0:
            raise ValueError('Поле процента отчислений врачу должно быть больше или равно 0')
        self.__percent = value

    # формирование строки таблицы
    def to_table_row(self) -> str:
        return u.green('║ ') + u.black_l(f'{self.__id:3}') + \
            u.green(' ║ ') + u.cyan(f'{self.person.surname:20}') + \
            u.green(' ║ ') + u.cyan(f'{self.person.name:20}') + \
            u.green(' ║ ') + u.cyan(f'{self.person.patronymic:20}') + \
            u.green(' ║ ') + u.cyan(f'{self.__speciality.name:20}') + \
            u.green(' ║ ') + u.cyan(f'{self.__price:15}') + \
            u.green(' ║ ') + u.cyan(f'{self.__percent:10.1f}') + u.green(' ║\n')

    # вывод шапки таблицы
    @staticmethod
    def show_header(title: str):
        print(
            u.green(
                '╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\n') +
            u.green('║ ') + u.purple(f'{title:^126}') + u.green(' ║\n') +
            u.green(
                '╠═════╦══════════════════════╦══════════════════════╦══════════════════════╦══════════════════════╦═════════════════╦════════════╣\n') +
            u.green('║ ') + u.purple(f'{"ID":^3}') +
            u.green(' ║ ') + u.purple(f'{"Фамилия":^20}') +
            u.green(' ║ ') + u.purple(f'{"Имя":^20}') +
            u.green(' ║ ') + u.purple(f'{"Отчество":^20}') +
            u.green(' ║ ') + u.purple(f'{"Специальность":^20}') +
            u.green(' ║ ') + u.purple(f'{"Цена приёма":^15}') +
            u.green(' ║ ') + u.purple(f'{"Процент":^10}') + u.green(' ║\n') +
            u.green(
                '╠═════╬══════════════════════╬══════════════════════╬══════════════════════╬══════════════════════╬═════════════════╬════════════╣'))

    # вывод подвала таблицы
    @staticmethod
    def show_footer():
        print(u.green(
            '╚═════╩══════════════════════╩══════════════════════╩══════════════════════╩══════════════════════╩═════════════════╩════════════╝'))

    # вывод таблицы
    @staticmethod
    def show_table(items: list, title: str = 'Все доктора'):
        Doctor.show_header(title)

        rows = ''
        for item in items:
            rows += item.to_table_row()
        print(rows, end='')

        Doctor.show_footer()
