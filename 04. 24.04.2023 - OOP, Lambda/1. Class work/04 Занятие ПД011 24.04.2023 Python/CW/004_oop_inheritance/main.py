# Наследование

# Пример использования наследования
from classes import Person, Employee


def main():
    # создание объекта класса Person
    person1 = Person('Варя', 23, 'Макеевка')
    print(person1)
    person1.plus_year()
    print(f'{person1.age} лет\n')

    # создание объекта производного класса Employee
    employee1 = Employee('Варя', 23, 'Макеевка', 'МакТТУ', 34_000)
    print(employee1)
    print(f'{employee1.age} лет, {employee1.salary}.00 руб.')

    # обращение к методу базового класса
    employee1.plus_year()
    print(f'{employee1.age} лет, {employee1.salary}.00 руб.')

    # обращение к методу класса
    employee1.twice_salary_plus_age()
    print(f'{employee1.age} лет, {employee1.salary}.00 руб.\n')

    # список объектов производного класса
    employees = [
        Employee('Борис', 21, 'Макеевка', 'МакТТУ', 34_000),
        Employee('Ярослава', 29, 'Снежное', 'ООО Рихтер', 67_000),
        Employee('Леонид', 43, 'Иловайск', 'ДонЖД', 32_000),
        Employee('Тамара', 41, 'Горловка', 'Горкоммунхоз', 23_000)
    ]

    for employee in employees:
        print(employee)
# end main


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)


