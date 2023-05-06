print('\n*** начало работы ***')

# Python поддерживает множество различных типов файлов, но условно
# их можно разделить на два вида: текстовые и бинарные. Текстовые
# файлы - это к примеру файлы с расширением cvs, txt, html, в общем
# любые файлы, которые сохраняют информацию в текстовом виде.
#
# Бинарные файлы - это изображения, аудио и видеофайлы и т.д. В зависимости от
# типа файла работа с ним может немного отличаться.
#
# При работе с файлами необходимо соблюдать некоторую последовательность операций:
# 1. Открытие файла с помощью метода open()
# 2. Чтение файла с помощью метода read() или запись в файл посредством метода write()
# 3. Закрытие файла методом close()

# Открытие и закрытие файла
# Чтобы начать работу с файлом, его надо открыть с помощью функции open(),
# которая имеет следующее формальное определение:
#        open(file, mode)
# Первый параметр функции представляет путь к файлу. Путь файла может быть
# абсолютным, то есть начинаться с буквы диска, например, C://somedir/somefile.txt.
# Либо можно быть относительным, например, somedir/somefile.txt - в этом случае поиск
# файла будет идти относительно расположения запущенного скрипта Python.
#
# Второй передаваемый аргумент - mode устанавливает режим открытия файла в зависимости
# от того, что мы собираемся с ним делать. Существует 4 общих режима:
#
# r (Read).  Файл открывается для чтения. Если файл не найден, то генерируется
#            исключение FileNotFoundError
#
# w (Write). Файл открывается для записи. Если файл отсутствует, то он создается.
#            Если подобный файл уже есть, то он создается заново, и соответственно
#            старые данные в нем стираются.
#
# a (Append). Файл открывается для дозаписи. Если файл отсутствует, то он создается.
#             Если подобный файл уже есть, то данные записываются в его конец.
#
# b (Binary). Используется для работы с бинарными файлами. Применяется вместе с другими
#             режимами - w или r.
#
# После завершения работы с файлом его обязательно нужно закрыть методом close().
# Данный метод освободит все связанные с файлом используемые ресурсы.

file_name = 'hello.txt'

# пример устаревшей работы с файлом
print('\nустаревшая работа с файлами... ', end='')
try:
    # encoding='UTF-8' - необязательный параметр, задает кодировку выводимого текста
    somefile = open(file_name, "w", encoding='UTF-8')
    try:
        somefile.write("hello, world\n")
        somefile.write("привет, мир\n")
        somefile.write("----------------\n")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)
print('Ok')

# более современный способ
# with open(file, mode) as file_obj:
#     инструкции
# Эта конструкция определяет для открытого файла переменную file_obj и выполняет
# набор инструкций. После их выполнения файл автоматически закрывается. Даже если
# при выполнении инструкций в блоке with возникнут какие-либо исключения, то файл
# все равно закрывается.

# дозапишем файл данных
print('более современный способ работы с файлами...', end='')
try:
    # encoding='UTF-8' - необязательный параметр, задает кодировку выводимого текста
    with open(file_name, "a", encoding='UTF-8') as somefile:
        somefile.write("hello, world\n")
        somefile.write("привет, мир\n")
        somefile.write("hello, happy world\n")
    # end with -- тут закрывается файл
except Exception as ex:
    print(ex)
print('Ok')

print('\n*** конец работы ***')