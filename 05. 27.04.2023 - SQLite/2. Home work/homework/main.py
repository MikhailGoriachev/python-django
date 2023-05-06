# библиотека для обработки нажатия клавиш
import keyboard

import app
import infrastructure.utils as u


def main():
    menu_commands = {
        0: exit,
        1: app.show_query01,
        2: app.show_query02,
        3: app.show_query03,
        4: app.show_query04,
        5: app.show_query05,
        6: app.show_query06,
        7: app.show_query07,
        8: app.show_appointments,
        9: app.show_doctors,
        10: app.show_patients,
        11: app.show_people,
        12: app.show_specialities
    }

    # текст меню
    menu = u.purple_l('\n\nМеню:\n') + \
           u.cyan_l('\t 1. Запрос 1\n') + \
           u.cyan_l('\t 2. Запрос 2\n') + \
           u.cyan_l('\t 3. Запрос 3\n') + \
           u.cyan_l('\t 4. Запрос 4\n') + \
           u.cyan_l('\t 5. Запрос 5\n') + \
           u.cyan_l('\t 6. Запрос 6\n') + \
           u.cyan_l('\t 7. Запрос 7\n\n') + \
           u.cyan_l('\t 8. Приёмы\n') + \
           u.cyan_l('\t 9. Доктора\n') + \
           u.cyan_l('\t10. Пациенты\n') + \
           u.cyan_l('\t11. Персоны\n') + \
           u.cyan_l('\t12. Специальности\n\n') + \
           u.red_l('\t0. Выход\n') + \
           u.blue_l('\nВведите номер пункта: ')

    # работа меню
    while True:
        try:
            # вывод пунктов меню
            print(menu, end='')

            # ввод команды
            command = (int(input()))

            print()

            # обработка команды
            menu_commands[command]()

            print(u.green_l('Нажмите [Enter] для выхода в меню...'))
            keyboard.wait('enter', True)
        except Exception as ex:
            print(u.red(ex))
            continue


if __name__ == '__main__':
    main()
