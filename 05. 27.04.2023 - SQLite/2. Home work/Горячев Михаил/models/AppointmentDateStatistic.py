from datetime import datetime

import infrastructure.utils as u


# Модель для записи статистики по дате приёма
class AppointmentDateStatistic:

    def __init__(self,
                 appointment_date: datetime,
                 min_price: int,
                 avg_price: float,
                 max_price: int,
                 amount: int):
        self.appointment_date = appointment_date
        self.min_price = min_price
        self.avg_price = avg_price
        self.max_price = max_price
        self.amount = amount

    # формирование строки таблицы
    def to_table_row(self) -> str:
        return u.green('║ ') + u.cyan(f'{u.get_local_format_date(self.appointment_date):15}') + \
            u.green(' ║ ') + u.cyan(f'{self.min_price:15}') + \
            u.green(' ║ ') + u.cyan(f'{self.avg_price:15.2f}') + \
            u.green(' ║ ') + u.cyan(f'{self.max_price:15}') + \
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
            u.green(' ║ ') + u.purple(f'{"Мин. цена":^15}') +
            u.green(' ║ ') + u.purple(f'{"Сред. цена":^15}') +
            u.green(' ║ ') + u.purple(f'{"Макс. цена":^15}') +
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
    def show_table(items: list, title: str = 'Статистика по дате приёма'):
        AppointmentDateStatistic.show_header(title)

        rows = ''
        for item in items:
            rows += item.to_table_row()
        print(rows, end='')

        AppointmentDateStatistic.show_footer()

    # получение данных из кортежа в модель
    @staticmethod
    def get_model_from_tuple(value: tuple):
        return AppointmentDateStatistic(
            u.get_date(value[0]),
            value[1],
            value[2],
            value[3],
            value[4]
        )
