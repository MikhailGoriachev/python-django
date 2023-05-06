# пример использования статических методов и статических атрибутов
from Triangle import Triangle


# главная функция - с нее начинаем выполнение приложения
def main():
    print('\n')

    # данные для формирования треугольника
    a, b, c = 3, -5, 6

    # вызов статического метода класса
    if Triangle.is_triangle(a, b, c):
        print(f'\t\033[32;1mВозможно создать треугольник со сторонами {a}, {b}, {c}\033[0m')
    else:
        print(f'\t\033[31;1mНевозможно создать треугольник со сторонами {a}, {b}, {c}\033[0m')
    # end if

    # создадим вспомогательный объект
    triangle = Triangle(4, 5, 6)

    # применение статических полей Triangle.header, Triangle.footer
    print(f'\n\n{Triangle.header}\n{triangle.to_table_row()}\n{Triangle.footer}\n')
# end main


# запуск главной функции приложения
if __name__ == '__main__':
    main()
# end if
