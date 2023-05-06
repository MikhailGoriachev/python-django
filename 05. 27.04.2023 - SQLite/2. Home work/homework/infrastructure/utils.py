from datetime import datetime

import babel.dates

from infrastructure import colors


# возвращение строки с указанным цветом
def color_string(string, color):
    return f'{color}{string}{colors.reset}'


# чёрная строка 
def black(string):
    return color_string(string, colors.black_bold)


# красная строка 
def red(string):
    return color_string(string, colors.red_bold)


# зелёная строка 
def green(string):
    return color_string(string, colors.green_bold)


# жёлтая строка 
def yellow(string):
    return color_string(string, colors.yellow_bold)


# синяя строка 
def blue(string):
    return color_string(string, colors.blue_bold)


# фиолетовая строка 
def purple(string):
    return color_string(string, colors.purple_bold)


# голубая строка 
def cyan(string):
    return color_string(string, colors.cyan_bold)


# белая строка 
def white(string):
    return color_string(string, colors.white_bold)


# ярко-чёрная строка 
def black_l(string):
    return color_string(string, colors.black_bold_bright)


# ярко-красная строка 
def red_l(string):
    return color_string(string, colors.red_bold_bright)


# ярко-зелёная строка 
def green_l(string):
    return color_string(string, colors.green_bold_bright)


# ярко-жёлтая строка 
def yellow_l(string):
    return color_string(string, colors.yellow_bold_bright)


# ярко-синяя строка 
def blue_l(string):
    return color_string(string, colors.blue_bold_bright)


# ярко-фиолетовая строка 
def purple_l(string):
    return color_string(string, colors.purple_bold_bright)


# ярко-голубая строка 
def cyan_l(string):
    return color_string(string, colors.cyan_bold_bright)


# ярко-белая строка 
def white_l(string):
    return color_string(string, colors.white_bold_bright)


# получения фамилии и инициалов из полных ФИО
def get_initials(surname: str, name: str, patronymic: str) -> str:
    return f'{surname} {name[0]}. {patronymic[0]}.'


# получения даты из строки 
def get_date(string_date: str) -> datetime:
    return datetime.strptime(string_date, '%Y-%m-%d')


# получения строкового представления даты 
def get_format_date(date: datetime) -> str:
    return date.strftime('%Y-%m-%d')


# получения строкового представления даты в локальном формате 
def get_local_format_date(date: datetime, locale='de_DE') -> str:
    return babel.dates.format_date(date, locale=locale)


if __name__ == "__main__":
    from main import main

    main()
