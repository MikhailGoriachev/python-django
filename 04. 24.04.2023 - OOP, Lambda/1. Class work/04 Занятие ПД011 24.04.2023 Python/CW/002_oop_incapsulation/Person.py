class Person:
    # методы класса
    # конструктор
    def __init__(self, name, age, city, pressure):
        self.__name = name            # атрибут имя персоны
        self.__age = age              # атрибут возраст
        self.__city = city            # атрибут город проживания
        self.__pressure = pressure    # атрибут кровяное давление
    # end __init__

    # вернуть возраст - чтение атрибута класса - такой метод называется геттер
    # или аксессор
    def getAge(self): return self.__age
    # end getAge

    # записать возраст - запись атрибута класса - такой метод называется сеттер
    # или мутатор
    def setAge(self, value):
        if value in range(1, 121):
            self.__age = value
        # end if
    # end setAge

    # Объявление свойства с использованием аннотаций/декораторов - 
    # рекомендуемый стиль реализации инкапсуляции
    # при этом геттер объявляется с аннотацией/декоратором @property
    # сеттер - @имя.setter
    @property
    def city(self): return self.__city

    @city.setter
    def city(self, value):
        if len(value) > 0:
            self.__city = value
        # end if
    # end city

    # пример свойства для доступа к атрибуту __name
    @property
    def name(self): return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise Exception('Попытка задать пустую строку в качестве имени')
        # end if

        self.__name = value
    # end name

    # давление - доступ к свойству при помощи геттера и сеттера
    # геттер
    # def getPressure(self):  return self.__pressure
    #
    # сеттер
    # def setPressure(self, value):
    #     if value < 60 or value > 250:
    #         raise Exception(f'Давление {value} вне допустимых значений [60, ..., 250]')
    #
    #     self.__pressure = value

    # давление - доступ к свойству при помощи аннотаций
    @property
    def pressure(self): return self.__pressure

    @pressure.setter
    def pressure(self, value):
        if 60 <= value <= 250:
            self.__pressure = value
        else:
            raise Exception(f'Давление {value} вне допустимых значений [60, ..., 250]')

    # Начиная с 3-й версии Python все классы неявно имеют один общий суперкласс
    # object и все классы по умолчанию наследуют его методы (о наследовании
    # говорим позже)
    # Одним из наиболее используемых методов класса object является метод
    # __str__(). Когда необходимо получить строковое представление объекта или
    # вывести объект в виде строки, то Python как раз вызывает этот метод. И при
    # определении класса хорошей практикой считается переопределение этого метода.
    def __str__(self):
        return f'имя {self.__name}, возраст {self.__age}, город {self.__city}, давление {self.__pressure}'
    # end __str__
# end class Person
