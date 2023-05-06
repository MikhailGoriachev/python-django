from sqlite3 import Cursor

from entities.Speciality import Speciality
from repositories.BaseRepository import BaseRepository


# Репозиторий специальностей
class SpecialitiesRepository(BaseRepository):
    TABLE_NAME = 'specialities'

    # все записи
    @staticmethod
    def get_all() -> list[Speciality]:
        sql = f'select * from {SpecialitiesRepository.TABLE_NAME}'
        cursor = BaseRepository.get_cursor().execute(sql)

        return SpecialitiesRepository.get_list_from_cursor(cursor)

    # получение данных из кортежа в модель
    @staticmethod
    def get_model_from_tuple(value: tuple) -> Speciality:
        return Speciality(value[0], value[1])

    # получение данных из курсора в виде списка
    @staticmethod
    def get_list_from_cursor(cursor: Cursor) -> list[Speciality]:
        data = []

        for v in cursor.fetchall():
            data.append(SpecialitiesRepository.get_model_from_tuple(v))

        return data
