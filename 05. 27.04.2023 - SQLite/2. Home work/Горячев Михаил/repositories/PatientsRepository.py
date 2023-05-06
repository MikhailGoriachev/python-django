from datetime import datetime
from sqlite3 import Cursor

from entities.Patient import Patient
from entities.Person import Person
from infrastructure import utils
from repositories.BaseRepository import BaseRepository


# Репозиторий пациентов
class PatientsRepository(BaseRepository):
    TABLE_NAME = 'view_patients'

    # все записи
    @staticmethod
    def get_all() -> list[Patient]:
        sql = f'select * from {PatientsRepository.TABLE_NAME}'
        cursor = BaseRepository.get_cursor().execute(sql)

        return PatientsRepository.get_list_from_cursor(cursor)

    # информация о пациентах с фамилиями, начинающимися на заданную параметром последовательность букв
    @staticmethod
    def get_all_by_surname_start_with(surname: str) -> list[Patient]:
        sql = f'select * from {PatientsRepository.TABLE_NAME} where person_surname like ?'
        cursor = BaseRepository.get_cursor().execute(sql, [surname + '%'])

        return PatientsRepository.get_list_from_cursor(cursor)

    # получение данных из кортежа в модель
    @staticmethod
    def get_model_from_tuple(value: tuple) -> Patient:
        return Patient(
            value[0],
            Person(value[1], value[2], value[3], value[4]),
            utils.get_date(value[5]),
            value[6],
            value[7]
        )

    # получение данных из курсора в виде списка
    @staticmethod
    def get_list_from_cursor(cursor: Cursor) -> list[Patient]:
        data = []

        for v in cursor.fetchall():
            data.append(PatientsRepository.get_model_from_tuple(v))

        return data
