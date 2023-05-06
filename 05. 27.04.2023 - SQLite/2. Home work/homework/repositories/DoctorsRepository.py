from datetime import datetime
from sqlite3 import Cursor

from entities.Doctor import Doctor
from entities.Person import Person
from entities.Speciality import Speciality
from repositories.BaseRepository import BaseRepository


# Репозиторий докторов
class DoctorsRepository(BaseRepository):
    TABLE_NAME = 'view_doctors'

    # все записи
    @staticmethod
    def get_all() -> list[Doctor]:
        sql = f'select * from {DoctorsRepository.TABLE_NAME}'
        cursor = BaseRepository.get_cursor().execute(sql)

        return DoctorsRepository.get_list_from_cursor(cursor)

    # информация о докторах, для которых значение в поле Процент отчисления на зарплату, больше заданного значения
    @staticmethod
    def get_all_by_percent_over(percent: float) -> list[Doctor]:
        sql = f'select * from {DoctorsRepository.TABLE_NAME} where percent > ?'
        cursor = BaseRepository.get_cursor().execute(sql, [percent])

        return DoctorsRepository.get_list_from_cursor(cursor)

    # информация о докторах, специальность которых задана параметром 
    @staticmethod
    def get_all_by_speciality(speciality_name: str) -> list[Doctor]:
        sql = f'select * from {DoctorsRepository.TABLE_NAME} where speciality_name like ?'
        cursor = BaseRepository.get_cursor().execute(sql, [speciality_name])

        return DoctorsRepository.get_list_from_cursor(cursor)

    # получение данных из кортежа в модель
    @staticmethod
    def get_model_from_tuple(value: tuple) -> Doctor:
        return Doctor(
            value[0],
            Person(value[1], value[2], value[3], value[4]),
            Speciality(value[5], value[6]),
            value[7],
            value[8]
        )

    # получение данных из курсора в виде списка
    @staticmethod
    def get_list_from_cursor(cursor: Cursor) -> list[Doctor]:
        data = []

        for v in cursor.fetchall():
            data.append(DoctorsRepository.get_model_from_tuple(v))

        return data
