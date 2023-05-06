from datetime import datetime

from entities.Doctor import Doctor
from entities.Patient import Patient

import infrastructure.utils as u


# Приём
class Appointment:

    def __init__(self,
                 _id: int,
                 appointment_date: datetime,
                 doctor: Doctor,
                 patient: Patient):
        self.__id = _id

        # дата приёма
        self.__appointment_date = appointment_date

        self.__patient = patient
        self.__doctor = doctor

    # id
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int):
        if not value >= 0:
            raise ValueError('Поле id должно быть больше либо равно 0')
        self.__id = value

    # дата приёма
    @property
    def appointment_date(self) -> datetime:
        return self.__appointment_date

    @appointment_date.setter
    def appointment_date(self, value: datetime):
        self.__appointment_date = value

    # доктор
    @property
    def doctor(self) -> Doctor:
        return self.__doctor

    @doctor.setter
    def doctor(self, value: Doctor):
        self.__doctor = value

    # пациент
    @property
    def patient(self) -> Patient:
        return self.__patient

    @patient.setter
    def patient(self, value: Patient):
        self.__patient = value

    # формирование строки таблицы
    def to_table_row(self) -> str:

        patient_name = u.get_initials(self.__patient.person.patronymic,
                                      self.__patient.person.name,
                                      self.__patient.person.surname)

        doctor_name = u.get_initials(self.__doctor.person.patronymic,
                                     self.__doctor.person.name,
                                     self.__doctor.person.surname)

        return u.green('║ ') + u.black_l(f'{self.__id:3}') + \
            u.green(' ║ ') + u.cyan(f'{u.get_local_format_date(self.__appointment_date):15}') + \
            u.green(' ║ ') + u.cyan(f'{patient_name:20}') + \
            u.green(' ║ ') + u.cyan(f'{self.__patient.passport:10}') + \
            u.green(' ║ ') + u.cyan(f'{doctor_name:25}') + \
            u.green(' ║ ') + u.cyan(f'{self.__doctor.price:15}') + \
            u.green(' ║ ') + u.cyan(f'{self.__doctor.percent:10.1f}') + u.green(' ║\n')

    # вывод шапки таблицы
    @staticmethod
    def show_header(title: str):
        print(
            u.green(
                '╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\n') +
            u.green('║ ') + u.purple(f'{title:^116}') + u.green(' ║\n') +
            u.green(
                '╠═════╦═════════════════╦══════════════════════╦════════════╦═══════════════════════════╦═════════════════╦════════════╣\n') +
            u.green('║ ') + u.purple(f'{"ID":^3}') +
            u.green(' ║ ') + u.purple(f'{"Дата приёма":^15}') +
            u.green(' ║ ') + u.purple(f'{"Пациент":^20}') +
            u.green(' ║ ') + u.purple(f'{"Паспорт":^10}') +
            u.green(' ║ ') + u.purple(f'{"Доктор":^25}') +
            u.green(' ║ ') + u.purple(f'{"Цена приёма":^15}') +
            u.green(' ║ ') + u.purple(f'{"Процент":^10}') + u.green(' ║\n') +
            u.green(
                '╠═════╬═════════════════╬══════════════════════╬════════════╬═══════════════════════════╬═════════════════╬════════════╣'))

    # вывод подвала таблицы
    @staticmethod
    def show_footer():
        print(u.green(
            '╚═════╩═════════════════╩══════════════════════╩════════════╩═══════════════════════════╩═════════════════╩════════════╝'))
        
    # вывод таблицы
    @staticmethod
    def show_table(items: list, title: str = 'Все приёмы'):
        Appointment.show_header(title)

        rows = ''
        for item in items:
            rows += item.to_table_row()
        print(rows, end='')

        Appointment.show_footer()
