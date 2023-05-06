import sqlite3
import main


def example():
     print("\nЗапрос к еще одной базе данных")
     connection = sqlite3.connect("db/subscriptions.db")
     cursor = connection.cursor()
     sql = """
         select
             editions.id
             , editions.title
             , editions.index_edition
             , type_editions.type 
             , editions.price 
         from 
             editions join type_editions on editions.id_type = type_editions.id
     """
     cursor.execute(sql)
     for row in cursor.fetchall():
          print(f"{row[0]:5} | {row[1]:25} | {row[2]:12} | {row[3]:12} | {row[4]:5} |")
     print()

     # использование кортежа для доступа к данным
     cursor.execute(sql)
     for (_id, title, index_edition, type, price) in cursor.fetchall():
          print(f"{_id:5} | {title:25} | {index_edition:12} | {type:12} | {price:5} |")


# запуск главной функции приложения
if __name__ == '__main__':
    main.main()
# end if