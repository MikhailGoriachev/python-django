import math
import infrastructure.utils as u

from models.figures.Figure3D import Figure3D


class Cylinder(Figure3D):
    __figure_name = 'Цилиндр'

    def __init__(self, radius: float, height: float) -> None:
        super().__init__('Цилиндр')
        self.__radius = radius
        self.__height = height

    # радиус
    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, value: float):
        if not value > 0:
            raise ValueError('Радиус должен быть больше 0')
        self.__radius = value

    # высота
    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, value: float):
        if not value > 0:
            raise ValueError('Высота должна быть больше 0')
        self.__height = value

    # площадь
    def area(self) -> float:
        return 2 * math.pi * self.__radius * (self.__height + self.__radius)

    # объём
    def volume(self) -> float:
        return math.pi * (self.__radius ** 2) * self.__height

    # вывод в строку таблицы 
    def to_table_row(self, n: int = 1) -> str:
        return u.green_l('║ ') + u.black_l(f'{n:3}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self._name:20}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.__height:20.3f}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.__radius:20.3f}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.area():20.3f}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.volume():20.3f}') + u.green_l(' ║\n')
