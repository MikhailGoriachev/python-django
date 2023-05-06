# доступ к классу Person
from Person import Person


# производный от Person класс Student
class Student(Person):

    # определение конструктора
    def __init__(self, name, age, city, university):
        # еще один способ вызова конструктора базового класса
        Person.__init__(self, name, age, city)

        self.__university = university                  # университет, в котром обучается студент
    # end __init__

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, value):
        self.__university = value

    # переопределение метода __str__()
    def __str__(self):
        return f'Студент {self.name} учится в университете {self.__university}'
    # end __str__
# end class Student
