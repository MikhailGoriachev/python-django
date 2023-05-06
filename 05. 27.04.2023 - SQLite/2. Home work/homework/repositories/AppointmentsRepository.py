from datetime import datetime
from sqlite3 import Cursor

from entities.Appointment import Appointment
from entities.Doctor import Doctor
from entities.Patient import Patient
from entities.Person import Person
from entities.Speciality import Speciality
from infrastructure import utils
from models.AppointmentDateStatistic import AppointmentDateStatistic
from models.AppointmentWithDoctorSalary import AppointmentWithDoctorSalary
from models.SpecialityStatistic import SpecialityStatistic
from repositories.BaseRepository import BaseRepository


# Репозиторий приёмов
class AppointmentsRepository(BaseRepository):
    TABLE_NAME = 'view_appointments'

    # все записи
    @staticmethod
    def get_all() -> list[Appointment]:
        sql = f'select * from {AppointmentsRepository.TABLE_NAME}'
        cursor = BaseRepository().get_cursor().execute(sql)

        return AppointmentsRepository.get_list_from_cursor(cursor)

    # информация о приемах за некоторый период, заданный параметрами
    @staticmethod
    def get_all_by_appointment_date_range(min_date: datetime, max_date: datetime) -> list[Appointment]:
        sql = f'select * from {AppointmentsRepository.TABLE_NAME} where appointment_date >= ? and appointment_date <= ?'
        cursor = BaseRepository().get_cursor().execute(sql, (
            utils.get_format_date(min_date), utils.get_format_date(max_date)))

        return AppointmentsRepository.get_list_from_cursor(cursor)

    # информация о приемах за некоторый период, заданный параметрами
    @staticmethod
    def get_all_with_salary() -> list[AppointmentWithDoctorSalary]:
        sql = f'select *, (price * percent / 100) - (price * percent / 100 * 0.13) as salary from {AppointmentsRepository.TABLE_NAME}'
        cursor = BaseRepository().get_cursor().execute(sql)

        data = []

        for v in cursor.fetchall():
            data.append(AppointmentWithDoctorSalary.get_model_from_tuple(v))

        return data

    # группировка по полю Дата приема. Для каждой даты вычисляет максимальную стоимость приема
    @staticmethod
    def group_by_appointment_date() -> list[SpecialityStatistic]:
        sql = f'select appointment_date, ' \
              f'     min(price) as min_price, ' \
              f'     avg(price) as avg_price, ' \
              f'     max(price) as max_price, ' \
              f'     count(*) as amount ' \
              f'from {AppointmentsRepository.TABLE_NAME} group by appointment_date'
        cursor = BaseRepository().get_cursor().execute(sql)

        data = []

        for v in cursor.fetchall():
            data.append(SpecialityStatistic.get_model_from_tuple(v))

        return data

    # группировка по полю Специальность. Для каждой специальности вычисляет средний Процент отчисления на зарплату от
    # стоимости приема
    @staticmethod
    def group_by_speciality() -> list[SpecialityStatistic]:
        sql = f'select doctor_speciality_name, ' \
              f'     min(percent) as min_percent, ' \
              f'     avg(percent) as avg_percent, ' \
              f'     max(percent) as max_percent, ' \
              f'     count(*) as amount ' \
              f'from {AppointmentsRepository.TABLE_NAME} group by doctor_speciality_name'
        cursor = BaseRepository().get_cursor().execute(sql)

        data = []

        for v in cursor.fetchall():
            data.append(SpecialityStatistic.get_model_from_tuple(v))

        return data

    # получение данных из кортежа в модель
    @staticmethod
    def get_model_from_tuple(value: tuple) -> Appointment:
        return Appointment(
            value[0],
            utils.get_date(value[1]),
            Doctor(value[2],
                   Person(value[3], value[4], value[5], value[6]),
                   Speciality(value[7], value[8]),
                   value[9],
                   value[10]),
            Patient(value[11],
                    Person(value[12], value[13], value[14], value[15]),
                    utils.get_date(value[16]),
                    value[17],
                    value[18]),
        )

    # получение данных из курсора в виде списка
    @staticmethod
    def get_list_from_cursor(cursor: Cursor) -> list[Appointment]:
        data = []

        for v in cursor.fetchall():
            data.append(AppointmentsRepository.get_model_from_tuple(v))

        return data
