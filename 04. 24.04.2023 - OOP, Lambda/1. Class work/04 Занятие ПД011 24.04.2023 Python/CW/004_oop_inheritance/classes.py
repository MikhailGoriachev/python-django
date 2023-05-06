# Наследование
# Наследование позволяет создавать новый класс на основе уже существующего
# класса. Наряду с инкапсуляцией наследование является одним из краеугольных
# камней объектно-ориентированного дизайна.
#
# Ключевыми понятиями наследования являются подкласс и суперкласс. Подкласс
# наследует от суперкласса все публичные атрибуты и методы. Суперкласс еще
# называется базовым (base class) или родительским (parent class),
# а подкласс - производным (derived class) или дочерним (child class).
#
# Синтаксис для наследования классов выглядит следующим образом:
# class подкласс (суперкласс):
#     методы_подкласса

class Person:
    # методы класса
    # конструктор
    def __init__(self, name, age, city):
        # атрибуты класса
        self.__name = name  # имя
        self.__age = age    # возраст
        self.__city = city  # город проживания
    # end __init__

    @property
    def age(self):  return self.__age

    @age.setter
    def age(self, age):
        if age not in range(1, 120):
            raise Exception(f'Недопустимое значение возраста {age}')
        # end if
        self.__age = age
    # end age

    @property
    def city(self):
        return self.__city
    # end city

    @city.setter
    def city(self, value):
        if len(value) > 0:
            self.__city = value
        # end if
    # end city

    @property
    def name(self):
        return self.__name
    # end name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise Exception('Имя не может быть пустым')
        # end if

        self.__name = value
    # end name

    # пример метода класса
    def plus_year(self):  self.__age += 1

    # Начиная с 3-й версии Python все классы неявно имеют один общий суперкласс
    # object и все классы по умолчанию наследуют его методы
    # Одним из наиболее используемых методов класса object является метод
    # __str__(). Когда необходимо получить строковое представление объекта или
    # вывести объект в виде строки, то Python как раз вызывает этот метод. И при
    # определении класса хорошей практикой считается переопределение этого метода.
    def __str__(self):
        return f'имя {self.__name}, возраст {self.__age}, город {self.__city}'
    # end __str__
# end class


# унаследуем класс Employee от класса Person
class Employee(Person):

    def __init__(self, name, age, city, company, salary):
        # вызов конструктора базового класса
        super().__init__(name, age, city)

        # задание атрибутов производного класса
        self.__company = company  # компания, атрибут производного класса
        self.__salary = salary    # оклад, атрибут производного класса
    # end __init__

    # свойства для доступа к атрибутам производного класса
    @property
    def company(self):
        return self.__company
    # end company

    @company.setter
    def company(self, value):
        if len(value) == 0:
            raise Exception('Название компании не может быть пустым')
        # end if

        self.__company = value
    # end company

    @property
    def salary(self):
        return self.__salary
    # end salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise Exception('Недопустимое значение оклада')
        # end if

        self.__salary = value
    # end salary

    # метод класса
    # удвоение оклада, увеличение возраста - работа с
    # атрибутом производного и методом базового класса в методе производного класса
    def twice_salary_plus_age(self):
        self.__salary *= 2
        self.plus_year()      # обращение к методу базового класса

    # строковое представление объекта класса
    def __str__(self):
        # super().__str__() - обращение к одноименному методу базового класса
        return f'{super().__str__()}, работает в {self.__company}, оклад {self.__salary}.00 руб.'
    # end __str__
# end class Employee

