# библиотека для обработки нажатия клавиш
import keyboard

import app
import infrastructure.utils as u


def main():
    menu_commands = {
        0: exit,
        1: app.point01,
        2: app.point02,
        3: app.point03
    }

    # текст меню
    menu = u.purple_l('\n\nМеню:\n') + \
           u.cyan_l('\t1. Самолёты\n') + \
           u.cyan_l('\t2. Животные\n') + \
           u.cyan_l('\t3. Фигуры\n') + \
           u.red_l('\t0. Выход\n') + \
           u.blue_l('\nВведите номер пункта: ')

    # работа меню
    while True:
        try:
            # вывод пунктов меню
            print(menu, end='')

            # обработка ввода команды
            menu_commands[(int(input()))]()

            print(u.green_l('Нажмите [Enter] для выхода в меню...'))
            keyboard.wait('enter', True)
        except ValueError:
            continue


if __name__ == '__main__':
    main()
