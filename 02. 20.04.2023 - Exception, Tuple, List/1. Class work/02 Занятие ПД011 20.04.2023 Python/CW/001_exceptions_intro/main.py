# Обработка исключений
# https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html

# Ошибки выполнения (runtime error) появляются в уже скомпилированной программе
# в процессе ее выполнения. Подобные ошибки еще называются исключениями.

# При возникновении исключения работа программы прерывается, и чтобы избежать подобного
# поведения и обрабатывать исключения в Python есть конструкция try..except..finally,
# которая имеет синтаксис
# try:
#     инструкции
# except [Тип_исключения1]:
#     инструкции_оработкиа_исключения_1
# except [Тип_исключения2]:
#     инструкции_оработкиа_исключения_1
# except [Тип_исключения3 as переменная]:
#     инструкции_оработкиа_исключения_3
# ...
# finally:
#     инструкции
import exceptions


def main():
    print(f'{__name__}: начало работы\n')

    try:
        # раскомментировать по одному для демонстрации работы исключений
        # простой пример

        # exceptions.exception1()

        # exceptions.exception2()

        # exceptions.exception3()

        # exceptions.exception4()

        exceptions.exception5()
    except Exception as ex:
        print(ex)
    finally:
        print(f'\n{__name__}: конец работы')
    # end try-except-finally
# end main


# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    main()
# end if
