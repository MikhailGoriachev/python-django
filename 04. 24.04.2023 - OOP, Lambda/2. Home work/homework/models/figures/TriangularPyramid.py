import math
import infrastructure.utils as u

from models.figures.Figure3D import Figure3D


class TriangularPyramid(Figure3D):
    __figure_name = 'Треугольная пирамида'

    def __init__(self, rib_length: float, base_length: float) -> None:
        super().__init__(TriangularPyramid.__figure_name)

        # длина основания
        self.__base_length = base_length

        # длина бокового ребра
        self.__rib_length = rib_length

    # длина основания
    @property
    def base_length(self) -> float:
        return self.__base_length

    @base_length.setter
    def base_length(self, value: float):
        if not value > 1:
            raise ValueError('Длина основания должна быть больше 0')
        self.__base_length = value

    # длина бокового ребра
    @property
    def rib_length(self) -> float:
        return self.__rib_length

    @rib_length.setter
    def rib_length(self, value: float):
        if not value > 1:
            raise ValueError('Длина бокового ребра должна быть больше 0')
        self.__rib_length = value

    # высота
    def height(self):
        return math.sqrt(self.__rib_length ** 2 - (self.__base_length / 2) ** 2)

    # площадь
    def area(self) -> float:
        return (math.sqrt(3) / 4) * self.__base_length ** 2 + \
            (3 / 2) * self.__base_length * math.sqrt(self.__rib_length ** 2 - (self.__base_length / 4))

    # объём
    def volume(self) -> float:
        return (self.height() * self.__base_length ** 2) / 4 * math.sqrt(3)

    # вывод в строку таблицы 
    def to_table_row(self, n: int = 1) -> str:
        return u.green_l('║ ') + u.black_l(f'{n:3}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self._name:20}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.__base_length:20.3f}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.__rib_length:20.3f}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.area():20.3f}') + \
            u.green_l(' ║ ') + u.cyan_l(f'{self.volume():20.3f}') + u.green_l(' ║\n')
