from datetime import datetime

from entities.Doctor import Doctor
from entities.Patient import Patient

import infrastructure.utils as u
from entities.Person import Person
from entities.Speciality import Speciality


# Модель для записи статистики по специальности
class SpecialityStatistic:

    def __init__(self,
                 speciality_name: str,
                 min_percent: int,
                 avg_percent: float,
                 max_percent: int,
                 amount: int):
        self.speciality_name = speciality_name
        self.min_percent = min_percent
        self.avg_percent = avg_percent
        self.max_percent = max_percent
        self.amount = amount

    # формирование строки таблицы
    def to_table_row(self) -> str:
        return u.green('║ ') + u.cyan(f'{self.speciality_name:15}') + \
            u.green(' ║ ') + u.cyan(f'{self.min_percent:15}') + \
            u.green(' ║ ') + u.cyan(f'{self.avg_percent:15.2f}') + \
            u.green(' ║ ') + u.cyan(f'{self.max_percent:15}') + \
            u.green(' ║ ') + u.cyan(f'{self.amount:15}') + u.green(' ║\n')

    # вывод шапки таблицы
    @staticmethod
    def show_header(title: str):
        print(
            u.green(
                '╔═════════════════════════════════════════════════════════════════════════════════════════╗\n') +
            u.green('║ ') + u.purple(f'{title:^87}') + u.green(' ║\n') +
            u.green(
                '╠═════════════════╦═════════════════╦═════════════════╦═════════════════╦═════════════════╣\n') +
            u.green('║ ') + u.purple(f'{"Дата приёма":^15}') +
            u.green(' ║ ') + u.purple(f'{"Мин. процент":^15}') +
            u.green(' ║ ') + u.purple(f'{"Сред. процент":^15}') +
            u.green(' ║ ') + u.purple(f'{"Макс. процент":^15}') +
            u.green(' ║ ') + u.purple(f'{"Количество":^15}') + u.green(' ║\n') +
            u.green(
                '╠═════════════════╬═════════════════╬═════════════════╬═════════════════╬═════════════════╣'))

    # вывод подвала таблицы
    @staticmethod
    def show_footer():
        print(u.green(
            '╚═════════════════╩═════════════════╩═════════════════╩═════════════════╩═════════════════╝'))

    # вывод таблицы
    @staticmethod
    def show_table(items: list, title: str = 'Статистика по специальностям'):
        SpecialityStatistic.show_header(title)

        rows = ''
        for item in items:
            rows += item.to_table_row()
        print(rows, end='')

        SpecialityStatistic.show_footer()

    # получение данных из кортежа в модель
    @staticmethod
    def get_model_from_tuple(value: tuple):
        return SpecialityStatistic(
            value[0],
            value[1],
            value[2],
            value[3],
            value[4],
        )
