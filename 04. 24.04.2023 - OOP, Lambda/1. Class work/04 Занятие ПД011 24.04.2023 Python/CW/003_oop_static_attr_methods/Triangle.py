import math


# Класс Треугольник, демонстрация статического метода,
# статического атрибута
class Triangle:
    # статический метод - существует в единственном экземпляре,
    # доступ без создания объекта класса,
    # синтаксис: ИмяКласса.имяМетода(параметры)
    # метод должен быть оснащен декоратором @staticmethod
    @staticmethod
    def is_triangle(a, b, c):
        # проверка треугольника на существование
        return a < b + c and b < a + c and c < a + b
    # end is_triangle

    # статический атрибут - атрибут, объявленный вне конструктора
    # без ключевого слова self, существует, в единственном экземпляре,
    # доступ без создания объекта класса,
    # синтаксис: ИмяКласса.имяАтрибута
    header = \
        '\t┌──────────────────────────┬────────────┬───────────────┐\n'\
        '\t│ Стороны треугольника     │ Периметр   │     Площадь   │\n'\
        '\t├──────────────────────────┼────────────┼───────────────┤'

    # статический атрибут класса - подвал таблицы
    footer = \
        '\t└──────────────────────────┴────────────┴───────────────┘'

    def __init__(self, a, b, c):
        # вызов статического метода
        # if not Triangle.is_triangle(a, b, c):
        if not self.is_triangle(a, b, c):
            raise AttributeError('некорректное значение сторон треугольника')

        self.__a = a      # сторона a треугольника
        self.__b = b      # сторона b треугольника
        self.__c = c      # сторона c треугольника
    # end __init__

    # кортеж для работы со всеми сторонами через одно свойство
    @property
    def sides(self):
        return self.__a, self.__b, self.__c

    @sides.setter
    def sides(self, value):    # value - кортеж
        if not self.is_triangle(value[0], value[1], value[2]):
            raise AttributeError('некорректное значение сторон треугольника')
        # end if
        self.__a, self.__b, self.__c = value[0], value[1], value[2]

    # периметр треугольника
    def perimeter(self):
        return self.__a + self.__b + self.__c
    # end perimeter

    # площадь треугольника
    def area(self):
        p = self.perimeter()
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))
    # end area

    # представление треугольника в текстовом формате
    def __str__(self):
        return f'Треугольник: {self.__a:.3f} x {self.__b:.3f}x{self.__c:.3f}, площадь = {self.area():.3f},' \
               f' периметр = {self.perimeter():.3f}'
    # end __str__

    # вывод данных треугольника в виде строки таблицы
    def to_table_row(self):
        sides = f'{self.__a:.3f} x {self.__b:.3f} x {self.__c:.3f}'
        return f'\t│ {sides:24} │ {self.perimeter():10.3f} │ {self.area():13.3f} │'
# end class Triangle
