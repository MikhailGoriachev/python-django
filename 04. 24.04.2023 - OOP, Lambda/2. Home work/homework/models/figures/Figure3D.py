import infrastructure.utils as u


class Figure3D:
    def __init__(self, name: str) -> None:
        # наименование фигуры
        self._name = name

    # наименование фигуры
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError('Наименование фигуры должно быть заполнено')
        self._name = value

    # площадь
    def area(self) -> float:
        pass

    # объём
    def volume(self) -> float:
        pass

    # вывод шапки таблицы
    @staticmethod
    def show_header(title: str):
        print(
            u.green_l(
                '╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\n') +
            u.green_l('║ ') + u.purple_l(f'{title:^118}') + u.green_l(' ║\n') +
            u.green_l(
                '╠═════╦══════════════════════╦══════════════════════╦══════════════════════╦══════════════════════╦══════════════════════╣\n') +
            u.green_l('║ ') + u.purple_l(f'{"N":^3}') +
            u.green_l(' ║ ') + u.purple_l(f'{"Фигура":^20}') +
            u.green_l(' ║ ') + u.purple_l(f'{"Высота/Основание":^20}') +
            u.green_l(' ║ ') + u.purple_l(f'{"Радиус/Ребро":^20}') +
            u.green_l(' ║ ') + u.purple_l(f'{"Площадь":^20}') +
            u.green_l(' ║ ') + u.purple_l(f'{"Объём":^20}') + u.green_l(' ║\n') +
            u.green_l(
                '╠═════╬══════════════════════╬══════════════════════╬══════════════════════╬══════════════════════╬══════════════════════╣'))

    # вывод подвала таблицы
    @staticmethod
    def show_footer():
        print(u.green_l(
            '╚═════╩══════════════════════╩══════════════════════╩══════════════════════╩══════════════════════╩══════════════════════╝'))

    # вывод таблицы
    @staticmethod
    def show_table(items: list, title: str):
        Figure3D.show_header(title)

        rows = ''
        for i in range(len(items)):
            rows += items[i].to_table_row(i + 1)
        print(rows, end='')

        Figure3D.show_footer()

    # вывод в строку таблицы 
    def to_table_row(self) -> str:
        pass
