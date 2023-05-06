# Базовый репозиторий
import sqlite3


class BaseRepository:
    # путь к базе данных
    DB_PATH = 'app_data/polyclinic.db'

    @staticmethod
    def get_cursor():
        return sqlite3.connect(BaseRepository.DB_PATH).cursor()
