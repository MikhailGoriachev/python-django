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


# вывод шапки таблицы
def show_array_header(title):
    size = 12

    headers_top_sep = green_l('╠')
    headers_index_vals = green_l('║ ')
    headers_bottom_sep = green_l('╠')

    for i in range(size - 1):
        headers_top_sep += green_l('═══════╦')
        headers_index_vals += f'{purple_l(f"{i:5}")}{green_l(" ║ ")}'
        headers_bottom_sep += green_l('═══════╬')

    headers_top_sep += green_l('═══════╣\n')
    headers_index_vals += f'{purple_l(f"{size - 1:5}")}{green_l(" ║")}\n'
    headers_bottom_sep += green_l('═══════╣')

    print(
        green_l(f'╔═{"":═^93}═╗\n') +
        green_l('║ ') + purple_l(f'{title:^93}') + green_l(' ║\n') +
        headers_top_sep + headers_index_vals + headers_bottom_sep)


# вывод строки таблицы
def show_list_rows(items: list):
    string = green_l('║ ')

    size = len(items)

    table_size_max = 12

    for i in range(table_size_max):
        if i < size:
            string += cyan_l(f'{items[i]:5}') + green_l(' ║ ')
        else:
            string += cyan_l(f'{"——":>5}') + green_l(' ║ ')

    print(string)


# вывод подвала таблицы
def show_list_footer(size=12):
    headers_bottom_sep = green_l('╚')

    for i in range(size - 1):
        headers_bottom_sep += green_l('═══════╩')

    headers_bottom_sep += green_l('═══════╝')

    print(green_l(headers_bottom_sep))


# вывод таблицы
def show_table(items: list, title):
    show_array_header(title)
    show_list_rows(items)
    show_list_footer()


if __name__ == "__main__":
    from main import main

    main()
