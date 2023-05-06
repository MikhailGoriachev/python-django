# полиморфизм

# Пример использования полиморфизма
from Person import Person
from Employee import Employee
from Student import Student


def main():
    # создание объекта класса Person
    person1 = Person('Варя', 23, 'Макеевка')
    print(person1)
    print(f'Возраст {person1.age} лет')
    print()

    # создание объекта производного класса Employee
    employee1 = Employee('Тимофей', 23, 'Макеевка', 'МакТТУ', 134_000)
    print(employee1)
    print(f'Возраст {employee1.age} лет')
    print()

    # создание объекта производного класса Student
    student1 = Student('Василиса', 34, 'Макеевка', 'ДонНАСА',)
    print(student1)
    print(f'Возраст {student1.age} лет')
    print()


    # Создание полиморфного списка
    people = [
        Person('Варя', 23, 'Макеевка'),
        Person('Юрий', 25, 'Енакиево'),
        Employee('Бронислава', 54, 'Макеевка', 'МакТТУ', 34_000),
        Employee('Федор', 43, 'Моспино', 'Старобешевская ТЭС', 54_000),
        Student('Семен', 23, 'Еленовка', 'ДонМУ'),
        Student('Ольга', 22, 'Докучаевск', 'ДонНТУ')
    ]

    print('\nВывод списка')
    for person in people:
        # Вызов метода базового класса доступен всей иерархии
        # person.plus_year()
        print(person)
    # end for

    # Проверка типа объекта - встроенная функция isinstance()
    print('\nИспользование встроенной функции \033[34misinstance()\033[0m')
    for person in people:
        if isinstance(person, Student):
            print(f'Student: {person.university}')
        elif isinstance(person, Employee):
            print(f'Employee: {person.company}')
        else:
            print(f'Person: {person.name}')

# end main


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# end if
