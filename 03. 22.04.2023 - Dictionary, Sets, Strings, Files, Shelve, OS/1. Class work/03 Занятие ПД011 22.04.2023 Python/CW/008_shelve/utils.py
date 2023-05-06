# формирование словаря с данными для решения задачи
import shelve

import main


def states_initialize():
    return {
        "Россия"   : "Москва",
        "Беларусь" : "Минск",
        "Молдова"  : "Кишинев",
        "Румыния"  : "Бухарест",
        "Турция"   : "Анкара",
        "Франция"  : "Париж",
        "Германия" : "Берлин",
        "Италия"   : "Рим",
        "Швейцария": "Берн",
        "Австрия"  : "Вена",
        "Куба"     : "Сантьяго",
        "Израиль"  : "Тель-Авив"
    }
# end states_initialize


# вывод словаря для описания стран
def show_states(title, states):
    # вывод шапки таблицы
    print(f'\t\033[30;1m{title}\n'
        '\t┌─────┬────────────────┬────────────────┐\n'
        '\t│  №  │ Название       │ Столица        │\n'
        '\t│ п/п │         страны │         страны │\n'
        '\t├─────┼────────────────┼────────────────┤')

    i = 1
    for state, capital in states.items():
        print(f'\t│ {i:3} │ {state:14} │ {capital:14} │')
        i += 1
    # end for

    # выводим подвал таблицы
    print('\t└─────┴────────────────┴────────────────┘\033[0m\n')
# end show_states


# чтение данных из бинарного файла в словарь при помощи модуля shelve
def read_to_dictionary(file_name):
    dict_states = {}

    with shelve.open(file_name) as states:
        for state in states:
            dict_states[state] = states[state]  # states[state] - собственно чтение
        # end for
    # end with

    return dict_states
# end read_to_dictionary


# запуск главной функции приложения
if __name__ == '__main__':
    main.main()
# end if
