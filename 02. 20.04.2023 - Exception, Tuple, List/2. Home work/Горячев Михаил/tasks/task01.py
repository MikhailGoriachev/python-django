import utils as u
import random


# Task1. Обработка кортежей. Описать функцию rect_ps(x1, y1, x2, y2), вычисляющую периметр и площадь прямоугольника 
# со сторонами, параллельными осям координат, по координатам (x1, y1), (x2, y2) его противоположных вершин (стороны 
# вычисляются как a = abs(x2 - x1), b = abs(y2 – y1)). Функция возвращает кортеж с периметром и площадью. С помощью 
# этой функции найти периметры и площади трех прямоугольников с данными противоположными вершинами.

# генерация прямоугольника
# возвращает кортеж вершин x1, y1, x2, y2
def create_rect():
    min_a, max_a, min_b, max_b = -10, 10, 20, 30
    return random.uniform(min_a, max_a), random.uniform(min_a, max_a), random.uniform(min_b, max_b), random.uniform(
        min_b, max_b)


# вычисления периметра и площади прямоугольника
def react_ps(x1, y1, x2, y2):
    a = abs(x2 - x1)
    b = abs(y2 - y1)

    return (a + b) * 2, a * b


# вывод шапки таблицы
def show_header():
    print(
        u.green_l('╔═══════════════════════════════════════════════════════════════════╗\n') +
        u.green_l('║ ') + u.purple_l(f'{"Задание 1. Прямоугольники":^65}') + u.green_l(' ║\n') +
        u.green_l('╠═════╦════════╦════════╦════════╦════════╦════════════╦════════════╣\n') +
        u.green_l('║ ') + u.purple_l(f'{"N":^3}') +
        u.green_l(' ║ ') + u.purple_l(f'{"x1":^6}') +
        u.green_l(' ║ ') + u.purple_l(f'{"y1":^6}') +
        u.green_l(' ║ ') + u.purple_l(f'{"x2":^6}') +
        u.green_l(' ║ ') + u.purple_l(f'{"y2":^6}') +
        u.green_l(' ║ ') + u.purple_l(f'{"Периметр":^10}') +
        u.green_l(' ║ ') + u.purple_l(f'{"Площадь":^10}') + u.green_l(' ║\n') +
        u.green_l('╠═════╬════════╬════════╬════════╬════════╬════════════╬════════════╣'))


# вывод строки таблицы
def show_row(n, item: tuple):
    print(
        u.green_l('║ ') + u.black_l(f'{n:3}') +
        u.green_l(' ║ ') + u.cyan(f'{item[0]:6.3f}') +
        u.green_l(' ║ ') + u.cyan(f'{item[1]:6.3f}') +
        u.green_l(' ║ ') + u.cyan(f'{item[2]:6.3f}') +
        u.green_l(' ║ ') + u.cyan(f'{item[3]:6.3f}') +
        u.green_l(' ║ ') + u.cyan_l(f'{item[4]:10.3f}') +
        u.green_l(' ║ ') + u.cyan_l(f'{item[5]:10.3f}') + u.green_l(' ║')
    )


# вывод подвала таблицы
def show_footer():
    print(u.green_l('╚═════╩════════╩════════╩════════╩════════╩════════════╩════════════╝'))


# вывод таблицы
def show_table(items):
    show_header()

    for i in range(len(items)):
        show_row(i + 1, items[i])

    show_footer()


if __name__ == "__main__":
    from main import main

    main()
