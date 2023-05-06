# Полиморфизм

# связь с базовым классом
from Person import Person


# унаследуем класс Employee от класса Person
class Employee(Person):

    def __init__(self, name, age, city, company, salary):
        # вызов конструктора базового класса, при таком формате вызова
        # передавать self не надо
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

    # строковое предстваление объекта класса
    def __str__(self):
        return f'{super().__str__()}, работает в {self.__company}, оклад {self.__salary}.00 руб.'
    # end __str__
# end class Employee




