from sqlite3 import Cursor

from entities.Person import Person
from repositories.BaseRepository import BaseRepository


# Репозиторий персон
class PeopleRepository(BaseRepository):
    TABLE_NAME = 'persons'

    # все записи
    @staticmethod
    def get_all() -> list[Person]:
        sql = f'select * from {PeopleRepository.TABLE_NAME}'
        cursor = BaseRepository.get_cursor().execute(sql)

        return PeopleRepository.get_list_from_cursor(cursor)

    # получение данных из кортежа в модель
    @staticmethod
    def get_model_from_tuple(value: tuple) -> Person:
        return Person(value[0], value[1], value[2], value[3])

    # получение данных из курсора в виде списка
    @staticmethod
    def get_list_from_cursor(cursor: Cursor) -> list[Person]:
        data = []

        for v in cursor.fetchall():
            data.append(PeopleRepository.get_model_from_tuple(v))

        return data
