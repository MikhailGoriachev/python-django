# модуль для демонстрации вариантов исключений

# обработка одного исключения
def exception1():
    try:
        number = int(input("Введите число: "))
        print("Введенное число:", number)
    except ValueError:
        print("Преобразование прошло неудачно")
# end exception1


# обработка нескольких исключений
def exception2():
    try:
        number1 = int(input("Введите первое число: "))
        number2 = int(input("Введите второе число: "))
        print("Результат деления:", number1 / number2)
    except ValueError:
        print("Преобразование прошло неудачно")
    except ZeroDivisionError:
        print("Попытка деления числа на ноль")
    except Exception:
        print("Общее исключение")
# end exception2


# пример использования finally
def exception3():
    try:
        number = int(input("Введите число: "))
        print("exception3: Введенное число:", number)
        return
    except ValueError:
        print("Не удалось преобразовать число")
    finally:
        print("exception3: Блок try завершил выполнение")
# end exception3


# поместить объект исключения в переменную
def exception4():
    try:
        number = int(input("Введите число: "))
        # ввод в заданной системе счисления: двоичная, вочтмеричная
        # и шестнадцатирирчная соотвтетсвенно
        # number = int(input("Введите число: "), 2)
        # number = int(input("Введите число: "), 8)
        # number = int(input("Введите число: "), 16)
        print("Введенное число:", number)
    except ValueError as e:
        print(f"Сведения об исключении: {e}")
# end exception4


# выброс исключения в коде - оператор raise
def exception5():
    try:
        number1 = int(input("Введите первое число: "))
        number2 = int(input("Введите второе число: "))

        if number2 == 0:
            raise Exception("Второе число не должно быть равно 0")

        print("Результат деления двух чисел:", number1 / number2)
    except ValueError:
        print("Введены некорректные данные")
    except Exception as e:
        print(e)
# end exception5


# исполняемый код для обеспечения запуска функции main()
# модулю, который стартует, всегда присваивается имя '__main__'
if __name__ == '__main__':
    from main import main
    main()
# end if
