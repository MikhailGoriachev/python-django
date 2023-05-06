# Модуль shelve
# Для работы с бинарными файлами в Python может применяться еще один
# модуль - shelve.
# Он сохраняет объекты в файл с определенным ключом. Затем по этому ключу
# может извлечь ранее сохраненный объект из файла. Процесс работы с данными
# через модуль shelve напоминает работу со словарями, которые также используют
# ключи для сохранения и извлечения объектов.

import shelve

# главная фукция для демонстрации модуля shelve
import utils

# C - create   - создание
# R - read     - чтение
# U - update   - изменение
# D - delete   - удаление
# CRUD - четыре базовые операции с коллекцией данных


def main():
    # имя файла для размещения словаря
    states_file_name = 'states'

    # формирование словаря для обработки
    dict_states = utils.states_initialize()

    # запись файла при помощи модуля shelve
    with shelve.open(states_file_name) as states:
        for state in dict_states:
            # 'states[state] =' вместе с присваиванием это и есть запись в файл
            states[state] = dict_states[state]
        # end for
    # end with
    print(f'\tФайл \033[34;1m{states_file_name}\033[0m данных записан')

    # чтение файла в словарь
    dict_states = utils.read_to_dictionary(states_file_name)

    # вывод словаря, прочитанного из файла
    utils.show_states(f'Файл \033[34;1m{states_file_name}\033[0m данных прочитан', dict_states)

    # добавить запись в файл
    with shelve.open(states_file_name) as states:
        # собственно запись
        states['Мексика'] = 'Мехико'

        # конечно, можно прямо тут прочитать данные в словарь, но
        # для чистоты кода мы этого делать не юудем...
    # end with

    # для контроля - читаем записи из файла в словарь
    # и вывод словаря с добавленной записью о Мексике
    dict_states = utils.read_to_dictionary(states_file_name)
    utils.show_states(f'Файл \033[34;1m{states_file_name}\033[0m данных с добавленной записью прочитан', dict_states)

    # изменение записи в файле
    with shelve.open(states_file_name) as states:
        # собственно изменение записи в файле - обращение по существующему ключу
        states['Мексика'] = 'Нью-Мехико'
    # end with

    # для контроля - читаем записи из файла в словарь
    # и ывод словаря с измененной записью о Мексике
    dict_states = utils.read_to_dictionary(states_file_name)
    utils.show_states(f'Измененный файл \033[34;1m{states_file_name}\033[0m данных прочитан', dict_states)

    # удаление записи в файле
    with shelve.open(states_file_name) as states:
        # удаление по ключу с одновременным получением данных
        state = 'Мексика'
        capital = states.pop(state, "Не найдено")
        print(f'\n\tУдалены данные о стране \033[32;1m{state}\033[0m - столица \033[32;1m{capital}\033[0m')

        # удаление записи по ключу при помощи оператора del
        state = 'Германия'
        capital = states[state]    # чтение из файла, для убобства вывода результатов

        del states[state]          # удаляем запись с ключом Германия
        print(f'\n\tУдалены данные о стране \033[32;1m{state}\033[0m - столица \033[32;1m{capital}\033[0m')
    # end with

    # для контроля - читаем записи из файла в словарь
    # вывод словаря с удаленными записями
    dict_states = utils.read_to_dictionary(states_file_name)
    utils.show_states(f'Файл \033[34;1m{states_file_name}\033[0m с удаленными записями', dict_states)

    # удаление всех записей в файле
    # with shelve.open(states_file_name) as states:
    #     states.clear()
    # end with

    # для контроля - читаем записи из файла в словарь
    dict_states = utils.read_to_dictionary(states_file_name)

    # вывод словаря с удаленными записями
    utils.show_states(f'Файл \033[34;1m{states_file_name}\033[0m с удаленными записями', dict_states)
# end main


# запуск главной функции приложения
if __name__ == '__main__':
    main()
# end if