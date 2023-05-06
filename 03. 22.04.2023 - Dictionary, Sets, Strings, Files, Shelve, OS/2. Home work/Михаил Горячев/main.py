# библиотека для обработки нажатия клавиш
import keyboard

import app
import infrastructure.utils as u


def main():
    commands = {
        0: exit,
        1: app.point01,
        2: app.point02,
        3: app.point03,
        4: app.point04
    }

    cmd = -1

    menu = u.purple_l('\n\nМеню:\n') + \
           u.cyan_l('\t1. Обработка множеств\n') + \
           u.cyan_l('\t2. Обработка строк, текстовых файлов\n') + \
           u.cyan_l('\t3. Обработка словарей, файлов в формате CSV\n') + \
           u.cyan_l('\t4. Бинарные файлы shelve, модуль os\n') + \
           u.red_l('\t0. Выход\n') + \
           u.blue_l('\nВведите номер пункта: ')

    while cmd != 0:

        try:
            print(menu, end='')

            # обработка ввода команды
            commands[(int(input()))]()

            print(u.green_l('Нажмите [Enter] для выхода в меню...'))
            keyboard.wait('enter', True)

        except ValueError:
            continue


if __name__ == '__main__':
    main()
