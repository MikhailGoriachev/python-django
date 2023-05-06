from infrastructure import utils as u
import random


# Task1. Обработка множеств. Разработайте функцию, в которой используются два множества из случайных целых чисел. 
# Функция должна обеспечивать:
#   — Формирование множеств – используйте операцию добавления в множество, длина каждого множества определяется 
#     генератором случайных чисел (от 5и до 23х элементов), диапазон значений элементов: -20, 20;
#   — Вычисление пересечения множеств;
#   — Вычисление разности множеств;
#   — Вычисление объединения множеств;
#   — Удаление всех отрицательных элементов из множества с меньшим количеством элементов 

# генерация множества
def create_set(n=random.randint(5, 23), min_val=-20, max_val=20):
    items = set()

    while True:
        items.add(random.randint(min_val, max_val))
        if len(items) == n:
            return items


# множества
set_values_a = create_set()
set_values_b = create_set()


# вычисление пересечения множеств
def get_intersection(set_a: set, set_b: set):
    return set_a & set_b


# вычисление разности множеств
def get_different(set_a: set, set_b: set):
    return set_a - set_b


# вычисление объединения множеств
def get_join(set_a: set, set_b: set):
    return set_a | set_b


# удаление всех отрицательных значений в множестве
def remove_negative(set_a: set):
    for v in set_a.copy():
        if v < 0:
            set_a.discard(v)


# вывод множества
def show_set(title, set_value: set):
    print(u.green_l(f'{title}:\n') + u.purple_l(set_value), end='\n\n')


if __name__ == "__main__":
    from main import main

    main()
