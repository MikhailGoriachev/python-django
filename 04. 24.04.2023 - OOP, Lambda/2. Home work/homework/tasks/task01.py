from models.Plane import Plane

# Task1. Разработайте класс Plane со следующими свойствами (созданными при помощи декораторов):
#   • тип самолета (Ил-76, Boeing-747, …)
#   • количество пассажирских мест (целое число, от 0 и выше)
#   • текущее количество пассажиров
#   • расход горючего за час полета (вещественное число, от 0 и выше)
#   • количество двигателей (целое число, от 1 до 12)
#   • название авиакомпании владельца самолета (непустая строка)
# В свойствах-сеттерах выбрасывайте исключение при некорректных значениях. Разработайте конструктор __init__() и 
# метод формирования строкового представления __str__() в виде строки таблицы.
# Создайте список самолетов (не менее 10 элементов). Разработайте функции для обработки списка:
#   •	Вывод списка самолетов в виде таблицы
#   •	Увеличение количества пассажиров на введенное с клавиатуры значение
#   •	Удаление выбранного по номеру в списке самолета 
#   •	Реализуйте сортировки списка самолетов:
#       o	По типу самолета
#       o	По убыванию количества двигателей
#       o	По названию авиакомпании владельца самолета
#       o	По убыванию расхода горючего за час полета

planes = [
    Plane('Ил-76', 200, 0, 5000, 4, 'Aeroflot'),
    Plane('Boeing-747', 416, 0, 15000, 4, 'Delta Air Lines'),
    Plane('Airbus A380', 853, 0, 17000, 4, 'Emirates'),
    Plane('Airbus A320', 180, 0, 2500, 2, 'Lufthansa'),
    Plane('Cessna 208B', 9, 0, 415, 1, 'Textron Aviation'),
    Plane('Embraer E175', 76, 0, 2000, 2, 'Republic Airways'),
    Plane('Dassault Falcon 7X', 16, 0, 1980, 3, 'Flexjet'),
    Plane('Gulfstream G650ER', 19, 0, 3000, 2, 'NetJets'),
    Plane('Bombardier 6000', 19, 0, 2000, 2, 'VistaJet'),
    Plane('Sikorsky S-76', 12, 0, 462, 2, 'Bristow Group')
]


# вывод всех записей
def show_all(title='Все самолёты'):
    Plane.show_table(planes, title)


# увеличение количества пассажиров
def increase_busy_places(n: int):
    for p in planes:
        p.busy_places += n


# удаление выбранного самолета
def remove_at(index: int) -> Plane:
    if len(planes) <= index:
        raise IndexError('Выход за пределы списка')

    plane = planes[index]
    planes.pop(index)

    return plane


# сортировка по типу самолета
def order_by_type_plane():
    return sorted(planes, key=lambda p: p.type_plane)


# сортировка по убыванию количества двигателей
def order_by_amount_engines_desc():
    return sorted(planes, key=lambda p: p.amount_engines, reverse=True)


# сортировка по названию авиакомпании владельца самолета
def order_by_owner():
    return sorted(planes, key=lambda p: p.owner)


# сортировка по убыванию расхода горючего за час полета
def order_by_consumption():
    return sorted(planes, key=lambda p: p.consumption)


if __name__ == "__main__":
    from main import main

    main()
