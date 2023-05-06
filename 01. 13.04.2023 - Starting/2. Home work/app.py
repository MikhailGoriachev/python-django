import functions
import random


# Proc17. Описать функцию roots_count(a, b, c), определяющую количество корней квадратного уравнения 
# a·x2 + b·x + c = 0 (a, b, c – параметры). Если коэффициент a равен нулю, то выбрасывать исключения. С помощью функции 
# roots_count() найти количество корней для каждого из трех квадратных уравнений с данными коэффициентами. 
# Коэффициенты a, b, c формировать генератором случайных чисел. Количество корней определять 
# по значению дискриминанта: d = b2 − 4·a·c.
def proc17():
    count = 3

    functions.show_header_proc17()

    min_value = -3
    max_value = 5

    for i in range(count):
        a = random.uniform(min_value, max_value)
        a = a if a > 0 else 0
        b = random.uniform(min_value, max_value)
        c = random.uniform(min_value, max_value)

        roots = functions.roots_count(a, b, c)

        functions.show_row_proc17(i + 1, a, b, c, roots)

    functions.show_footer_proc17()


# Proc21. Описать функцию sum_range(a, b), находящую сумму всех целых чисел от A до B включительно (a и b – целые). 
# Если a > b, то выбрасывать исключение. С помощью функции sum_range() найти суммы для пяти пар случайных чисел.
def proc21():
    count = 3

    functions.show_header_proc21()

    min_value = -20
    max_value = 20

    for i in range(count):
        a = random.randint(min_value, max_value)
        b = random.randint(min_value, max_value)

        result = functions.sum_range(a, b)

        functions.show_row_proc21(i + 1, a, b, result)

    functions.show_footer_proc21()


# Proc28. Описать функцию is_prime(n), возвращающую True, если параметр n является простым числом, и False в 
# противном случае (число, большее 1, называется простым, если оно не имеет положительных делителей, кроме 1 и самого
# себя). Если параметр n <= 1, то выбрасывать исключение. C помощью функции is_prime() найти количество простых чисел
# среди 15 случайных чисел в диапазоне от -120 до 250.
def proc28():
    count = 15

    functions.show_header_proc28()

    min_value = -120
    max_value = 250

    for i in range(count):
        a = random.randint(min_value, max_value)

        result = functions.is_prime(a)

        functions.show_row_proc28(i + 1, a, result)

    functions.show_footer_proc28()


if __name__ == "__main__":
    from main import main

    main()
