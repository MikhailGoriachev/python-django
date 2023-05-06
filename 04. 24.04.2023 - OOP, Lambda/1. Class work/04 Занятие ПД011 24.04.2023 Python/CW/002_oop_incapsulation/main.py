# Инкапсуляция
# Инкапсуляция является фундаментальной концепцией объектно-ориентированного
# программирования. Она предотвращает прямой доступ к атрибутам объекта из
# вызывающего кода.

# Реализация инкапсуляции в языке программирования Python: скрыть атрибуты
# класса можно сделав их приватными или закрытыми и ограничив доступ к ним
# через специальные методы, которые еще называются свойствами.

from Person import Person


def main():
    # создание объекта класса Person
    person1 = Person('Варя', 23, 'Макеевка', 100)
    print(person1)

    # !!! вот тут создаются новые атрибуты конкретного объекта !!!
    # person1.__name = 'Борис'
    # person1.__age = 1200
    # print(person1)
    # print(f'{person1.__name} {person1.__age}')


    person1.setAge(98)
    print(person1)

    person1.setAge(person1.getAge()+1)
    print(person1)

    # пример записи некорректных данных
    person1.setAge(person1.getAge()+10_000)
    print(person1)

    # запись атрибута  __city при помощи свойства city
    person1.city = 'Донецк'
    print(f'Город изменен на {person1.city}, персона: {person1}')


    # person1.setPressure(300)
    # запись атрибута  __pressure при помощи свойства pressure
    person1.pressure = 120
    print(f'{person1}')

    # сравнение аксессоров и мутаторов со свойствами, заданными аннотацией
    # запись атрибута  __age при помощи мутатора
    person1.setAge(25)
    print(f'{person1.getAge()} <<<<<<')


    # добавлен атрибут конкретному объекту
    person1.street = 'ул. Таманская'

    # чтение атрибута __age при помощи геттера, чтение атрибута __city
    # при помощи свойства city
    print(f'{person1.getAge()} {person1.city} {person1.street}')
    print()


    # создание списка объектов
    people = [
        Person('Федор', 21, "Донецк", 90),
        Person('Варя', 38, "Енакиево", 110),
        Person('Семен', 43, "Горловка", 100)
    ]

    print('\nПример вывода при помощи __str__():')
    for person in people:
        print(person)

    print('\nПример вывода с доп. информацией:')
    for person in people:
        print(f'{person.name} из города {person.city} имеет давление {person.pressure} в возрасте {person.getAge()} лет')
        # print(person)

    # свойства конкретного объекта меняем, но сам объкет - нет
    for person in people:
        person.pressure = 80

    print('\nПример вывода при помощи __str__():')
    for person in people:
        print(person)

# end main


# запуск главной функции приложения
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Ошибка: {e}')
# end if
