# Модуль OS и работа с файловой системой
import os

# Ряд возможностей по работе с каталогами и файлами предоставляет встроенный
# модуль os. Хотя он содержит много функций, рассмотрим только основные из них:
#
# mkdir()  : создает новую папку
# rmdir()  : удаляет папку
# rename() : переименовывает файл
# remove() : удаляет файл


def main():
    # Создание и удаление папки
    # Для создания папки применяется функция mkdir(), в которую передается путь
    # к создаваемой папке

    # путь относительно текущего скрипта
    os.mkdir("hello")

    # абсолютный путь к создаваемой папке
    os.mkdir("d:/somedir")
    os.mkdir("d:/somedir/hello")
    str1 = input('?')

    # Для удаления папки используется функция rmdir(), в которую передается
    # путь к удаляемой папке:

    # путь относительно текущего скрипта
    os.rmdir('hello')

    # абсолютный путь к удаляемой папке
    os.rmdir("d:/somedir/hello")
    os.rmdir("d:/somedir")
    str1 = input('?')

    # Переименование файла
    # Для переименования вызывается функция rename(source, target), первый параметр
    # которой - путь к исходному файлу, а второй - новое имя файла. В качестве
    # путей могут использоваться как абсолютные, так и относительные.
    # Например, пусть в папке d:/data/ располагается файл somefile.txt. Переименуем
    # его в файл "hello.txt":

    os.rename("d:/data/somedata.txt", "d:/data/hello.txt")

    # Удаление файла
    # Для удаления вызывается функция remove(), в которую передается путь к файлу:
    os.remove("d:/data/hello.txt")

    # Существование файла
    # Если мы попытаемся открыть файл, который не существует, то Python выбросит
    # исключение FileNotFoundError. Для отлова исключения мы можем использовать
    # конструкцию try...except. Однако можно уже до открытия файла проверить,
    # существует ли он или нет с помощью метода os.path.exists(path).
    # В этот метод передается путь, который необходимо проверить:
    filename = "d:/data/hello.txt"

    str1 = "" if os.path.exists(filename) else "не"
    print(f"\nФайл {filename} {str1} существует")
# end main


# запуск главной функции приложения
if __name__ == '__main__':
    main()
# end if
