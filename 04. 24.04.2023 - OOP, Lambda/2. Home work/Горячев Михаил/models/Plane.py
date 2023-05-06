from infrastructure import utils as u


class Plane:
    def __init__(self, type_plane: str = 'нет данных',
                 place_capacity: int = 0,
                 busy_place: int = 0,
                 consumption: float = 0,
                 amount_engines: int = 1,
                 owner: str = 'нет данных') -> None:
        self.__type_plane = type_plane
        self.__place_capacity = place_capacity
        self.__busy_places = busy_place
        self.__consumption = consumption
        self.__amount_engines = amount_engines
        self.__owner = owner

    # тип самолета (Ил-76, Boeing-747, …)
    @property
    def type_plane(self) -> str:
        return self.__type_plane

    @type_plane.setter
    def type_plane(self, value: str):
        if not len(value) > 0:
            raise ValueError('Тип самолёта должен быть заполнен')
        self.__type_plane = value

    # количество пассажирских мест (целое число, от 0 и выше)
    @property
    def place_capacity(self) -> int:
        return self.__place_capacity

    @place_capacity.setter
    def place_capacity(self, value: int):
        if not value >= 0:
            raise ValueError('Количество пассажирских мест должно быть от 0 и выше')
        self.__place_capacity = value

    # текущее количество пассажиров
    @property
    def busy_places(self) -> int:
        return self.__busy_places

    @busy_places.setter
    def busy_places(self, value: int):
        if not value <= self.__place_capacity >= 0:
            raise ValueError(f'Количество пассажиров не может быть больше вместимости ({self.__place_capacity} мест)')
        self.__busy_places = value

    # расход горючего за час полета (вещественное число, от 0 и выше)
    @property
    def consumption(self) -> float:
        return self.__consumption

    @consumption.setter
    def consumption(self, value: float):
        if not value >= self.__place_capacity:
            raise ValueError(f'Расход горючего за час полета должно быть от 0 и выше')
        self.__consumption = value

    # количество двигателей (целое число, от 1 до 12)
    @property
    def amount_engines(self) -> int:
        return self.__amount_engines

    @amount_engines.setter
    def amount_engines(self, value: int):
        if not value >= self.__place_capacity:
            raise ValueError(f'Количество двигателей от 1 до 12')
        self.__amount_engines = value

    # название авиакомпании владельца самолета (непустая строка)
    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, value: str):
        if not len(value) > 0:
            raise ValueError('Название авиакомпании владельца должно быть заполнено')
        self.__owner = value

    # строковое представление объекта для таблицы
    def __str__(self, n: int = 1) -> str:

        return u.green_l('║ ') + u.black_l(f'{n:3}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.__type_plane:30}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.__place_capacity:15}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.__busy_places:15}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.__consumption:15}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.__amount_engines:10}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.__owner:20}') + u.green_l(' ║\n')

    # вывод шапки таблицы
    @staticmethod
    def show_header(title: str):
        print(
            u.green_l(
                '╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\n') +
            u.green_l('║ ') + u.purple_l(f'{title:^126}') + u.green_l(' ║\n') +
            u.green_l(
                '╠═════╦════════════════════════════════╦═════════════════╦═════════════════╦═════════════════╦════════════╦══════════════════════╣\n') +
            u.green_l('║ ') + u.purple_l(f'{"N":^3}') +
            u.green_l(' ║ ') + u.purple_l(f'{"Тип самолёта":^30}') +
            u.green_l(' ║ ') + u.purple_l(f'{"Пассаж. места":^15}') +
            u.green_l(' ║ ') + u.purple_l(f'{"Занято мест":^15}') +
            u.green_l(' ║ ') + u.purple_l(f'{"Расход топлива":^15}') +
            u.green_l(' ║ ') + u.purple_l(f'{"Двигатели":^10}') +
            u.green_l(' ║ ') + u.purple_l(f'{"Владелец":^20}') + u.green_l(' ║\n') +
            u.green_l(
                '╠═════╬════════════════════════════════╬═════════════════╬═════════════════╬═════════════════╬════════════╬══════════════════════╣'))

    # вывод подвала таблицы
    @staticmethod
    def show_footer():
        print(u.green_l(
            '╚═════╩════════════════════════════════╩═════════════════╩═════════════════╩═════════════════╩════════════╩══════════════════════╝'))

    # вывод таблицы
    @staticmethod
    def show_table(items: list, title: str):
        Plane.show_header(title)

        rows = ''
        for i in range(len(items)):
            rows += items[i].__str__(i + 1)
        print(rows, end='')

        Plane.show_footer()
