import math
import colors as clr


# вычисление количества квадратных корней
def roots_count(a, b, c):
    if a == 0:
        return "Нет корней"

    d = (b ** 2) - 4 * a * c

    if d < 0:
        return 0
    elif d > 0:
        return 2
    else:
        return 1


# вывод заголовка для таблицы квадратных уравнений
def show_header_proc17():
    print(f'''{clr.green_bold}
    ╔════════════════════════════════════════════╗
    ║ {'Задача Proc17. Квадратные корни':^42} ║
    ╠════╦════════╦════════╦════════╦════════════╣
    ║ N  ║ A      ║ B      ║ C      ║ Количество ║
    ║    ║        ║        ║        ║ корней     ║
    ╠════╬════════╬════════╬════════╬════════════╣{clr.reset}
''', end='')


# вывод строки для таблицы квадратных уравнений
def show_row_proc17(n, a, b, c, amount):
    result_color = clr.cyan_bold if isinstance(amount, int) else clr.red_bold

    print(f'\t'
          f'{clr.green_bold}║{clr.reset} '
          f'{n:>2} {clr.green_bold}║ {clr.reset}'
          f'{a:>6.3f} {clr.green_bold}║ {clr.reset}'
          f'{b:>6.3f} {clr.green_bold}║ {clr.reset}'
          f'{c:>6.3f} {clr.green_bold}║ {clr.reset}'
          f'{result_color}{(amount if isinstance(amount, int) else "a == 0"):>10} {clr.green_bold}║{clr.reset}')


# вывод подвала для таблицы квадратных уравнений
def show_footer_proc17():
    print(f'\t{clr.green_bold}╚════╩════════╩════════╩════════╩════════════╝{clr.reset}')


# сумма чисел в диапазоне
def sum_range(a, b):
    if a > b:
        return 'a > b'

    result = sum(range(a, b + 1))

    return result


# вывод заголовка для таблицы суммы чисел в диапазоне
def show_header_proc21():
    print(f'''{clr.green_bold}
    ╔═════════════════════════════════════════╗
    ║ {'Задача Proc21. Сумма чисел в диапазоне':^39} ║
    ╠════╦══════════╦══════════╦══════════════╣
    ║ N  ║ A        ║ B        ║ Сумма        ║
    ╠════╬══════════╬══════════╬══════════════╣{clr.reset}
''', end='')


# вывод строки для таблицы суммы чисел в диапазоне
def show_row_proc21(n, a, b, result):
    result_color = clr.cyan_bold if isinstance(result, int) else clr.red_bold

    print(f'\t'
          f'{clr.green_bold}║{clr.reset} '
          f'{n:>2} {clr.green_bold}║ {clr.reset}'
          f'{a:>8} {clr.green_bold}║ {clr.reset}'
          f'{b:>8} {clr.green_bold}║ {clr.reset}'
          f'{result_color}{result:>12} {clr.green_bold}║ {clr.reset}')


# вывод подвала для таблицы суммы чисел в диапазоне
def show_footer_proc21():
    print(f'\t{clr.green_bold}╚════╩══════════╩══════════╩══════════════╝{clr.reset}')


# проверка числа на то является ли число простым
def is_prime(n):
    if n <= 1:
        return "Число <= 2"

    for i in range(2, int(math.sqrt(n))):
        if (n % i) == 0:
            return False

    return True


# вывод заголовка для таблицы простого числа
def show_header_proc28():
    print(f'''{clr.green_bold}
    ╔════════════════════════════════╗
    ║ {'Задача Proc28. Простое число':^30} ║
    ╠════╦══════════╦════════════════╣
    ║ N  ║ A        ║ Простое        ║
    ╠════╬══════════╬════════════════╣{clr.reset}
''', end='')


# вывод строки для таблицы простого числа
def show_row_proc28(n, a, result):
    is_bool = isinstance(result, bool)

    if is_bool and result:
        result_color = clr.cyan_bold
        result = 'да'
    else:
        result_color = clr.red_bold
        result = 'нет' if is_bool else result

    print(f'\t'
          f'{clr.green_bold}║{clr.reset} '
          f'{n:>2} {clr.green_bold}║ {clr.reset}'
          f'{a:>8} {clr.green_bold}║ {clr.reset}'
          f'{result_color}{result:>14} {clr.green_bold}║ {clr.reset}')


# вывод подвала для таблицы простого числа
def show_footer_proc28():
    print(f'\t{clr.green_bold}╚════╩══════════╩════════════════╝{clr.reset}')


if __name__ == '__main__':
    from main import main

    main()
