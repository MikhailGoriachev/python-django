import random

from models.figures.Figure3D import Figure3D
from models.figures.Conoid import Conoid
from models.figures.Cylinder import Cylinder
from models.figures.TriangularPyramid import TriangularPyramid

# Task 3. Создать иерархию классов:
# •	Базовый класс Фигура3D со свойством радиус, пустыми методами для вычисления площади и объема (имеются в виду 
#   объявления вида def area(): pass и def volume(): pass)
# •	Класс Цилиндр, наследует от Фигура3D с методами для вычисления площади и объема
# •	Класс Конус, наследует от Фигура3D с методами для вычисления площади и объема
# •	Класс ТрехграннаяПирамида, наследует от Фигура3D с методами для вычисления площади и объема (правильная 
#   трехгранная пирамида для упрощения вычислений)
# •	реализовать по два объекта каждого типа в списке наследников класса Фигура3D, вычислить суммарную площадь фигур, 
#   суммарный объем фигур


figures = [
    Conoid(random.uniform(3, 7), random.uniform(10, 12)),
    Conoid(random.uniform(3, 7), random.uniform(10, 12)),
    Cylinder(random.uniform(3, 7), random.uniform(10, 12)),
    Cylinder(random.uniform(3, 7), random.uniform(10, 12)),
    TriangularPyramid(random.uniform(3, 7), random.uniform(3, 7)),
    TriangularPyramid(random.uniform(3, 7), random.uniform(3, 7))
]


# вывод всех записей
def show_all(title='Фигуры'):
    Figure3D.show_table(figures, title)


# сумма площадей
def get_sum_area():
    return sum(map(lambda f: f.area(), figures))


# сумма объёмов
def get_sum_volume():
    return sum(map(lambda f: f.volume(), figures))


if __name__ == "__main__":
    from main import main

    main()
