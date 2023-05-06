# работаем с SQLite
# https://python-scripts.com/sqlite
import sqlite3

# модуль с ф-ми для работы с существующей БД
from subscriptions import example


# вывод всех строк/записей таблицы на открытом курсоре
def show_all_rows(title, read_cursor, table_name='albums'):
    print(title)
    for row in read_cursor.execute(f"select * from {table_name}"):
        print(row)
    print('Ok\n')


def main():
    # путь к базе данных и имя файла данных или вместо этого укажите
    # :memory: чтобы сохранить в RAM

    db_path = "db/example_database.db"
    # db_path = ":memory:"

    # имя таблицы данных
    table_name = "albums"

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()  # cursor CURrent Set Of Rows

    # Пример создания таблицы
    cursor.execute(
        f"""create table if not exists {table_name} (
               id integer primary key autoincrement, 
               title text, 
               artist text, 
               release_date text,
               publisher text, 
               media_type text)
        """)
    print('create table: Ok\n')

    # Вставка данных в таблицу - один оператор для одной записи
    # Возвращается также курсор
    res = cursor.execute(
        f"""insert into {table_name} 
              (title, artist, release_date, publisher, media_type)
          values 
              ('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3')
        """
    )
    print(f'Добавлено записей: {res.rowcount}')

    # Сохраняем изменения
    conn.commit()
    print('Вставка одной записи: Ok\n')


    # Вставляем множество данных в таблицу используя безопасный метод "?"
    albums = [
        ('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
        ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
        ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
        ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')
    ]

    cursor.executemany(
        f"insert into {table_name} (title, artist, release_date, publisher, media_type) values (?,?,?,?,?)",
        albums
    )
    conn.commit()
    print('Вставка нескольких записей: Ok\n')

    # покажем все записи после вставки
    show_all_rows(f"Все записи таблицы \033[4m{table_name}\033[0m", cursor)


    # Обновление записей
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    sql = f"""
        update {table_name} 
        set artist = ? 
        where artist = ?
    """

    # параметры в порядке их появления в запросе
    # set artist = 'John Doe'
    # where artist = 'Andy Hunter'
    cursor.execute(sql, ('John Doe', 'Andy Hunter'))
    conn.commit()

    print('Изменение записи/записей: Ok\n')
    show_all_rows(f"Все записи таблицы \033[4m{table_name}\033[0m после изменения", cursor)


    # удаление записей
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    sql = f"delete from {table_name} where artist = ?"
    res = cursor.execute(sql, [('John Doe')])
    conn.commit()
    print(f'Удаление: Ok, удалено записей {res.rowcount}\n')
    show_all_rows(f"Все записи таблицы \033[4m{table_name}\033[0m после удаления", cursor)


    # чтение данных
    # читаем одну запись
    print('\nЧтение одной записи:')
    conn = sqlite3.connect(db_path)
    # conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = f"select * from {table_name} where artist=?"
    cursor.execute(sql, [("Red")])
    # print(cursor.fetchall()) # чтение всез выбранных записей
    print(cursor.fetchone())  # чтение первой записи из всех выбранных
    print('чтение одной записи: Ok\n')


    print("\nПример запроса на выборку с использованием LIKE:")
    sql = f"select * from {table_name} where title like ?"
    result = cursor.execute(sql, [('The %')])

    # так рекомендуется
    # for row in cursor.fetchall():
    #     print(row)

    # result - ссылка на cursor, после итерации по cursor
    # переменная result показывает за выборку...
    for row in result.fetchall():
        print(row)
    print('запрос выполнен\n')

    # запрос к еще одной базе данных
    example()


# запуск главной функции приложения
if __name__ == '__main__':
    main()
# end if