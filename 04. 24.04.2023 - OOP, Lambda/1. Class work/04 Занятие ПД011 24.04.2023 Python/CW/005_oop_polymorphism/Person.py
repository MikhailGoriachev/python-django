# базовый класс иерархии
class Person:
    # методы класса
    # конструктор
    def __init__(self, name, age, city):
        self.__name = name    # имя
        self.__age = age      # возраст
        self.__city = city    # город проживания
    # end __init__

    @property
    def age(self):
        return self.__age
    # end age

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
    def plus_year(self):
        self.__age += 1

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

