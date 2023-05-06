# Вспомогательные функции
import random


# вывод list в одну строку с заголовком title
def show_list(list, title):
    str1 = title + '['

    # доступ только по чтению - итератор
    # list - итерируемый объект
    for item in list:
        # str1 += str(item) + ' '
        str1 += f'{item} '
    str1 += ']'
    print(str1)
# end def


# Заполнение списка случайными числами
# доступ к элементам списка через индексирование: 
# доступ и по чтению и по записи
def fill_list(list, low, high):
    # длина списка через свойство объекта
    # for i in range(0, list.__len__()):

    # длина списка через внешнюю функцию len(объект)
    for i in range(0, len(list)):
        list[i] = random.randint(low, high+1)
# end def
