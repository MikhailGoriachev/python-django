from infrastructure import utils as u
import csv

# Task2. Обработка строк, текстовых файлов. Для файла text.txt, приведенного в папке задания реализуйте обработки 
# (файл скопируйте в Ваш проект при создании проекта):
#   — Перевести текст из исходного файла в нижний регистр, сохранить в файле lowers.txt
#   — В файле lowers.txt подсчитать количество строк, слов, определить максимальную длину слова и список слов 
#     максимальной длины, минимальную длину слова и список слов минимальной длины, сохраните списки слов в файлах 
#     longest.txt и shortest.txt соответственно для слов максимальной и минимальной длины
#   — Сформируйте словарь из слов файла lowers.txt – ключом является слово, значением – количество вхождений этого слова 
#     в текст. Сохраните этот словарь в формате CSV, имя файла words.csv


# названия файлов
text_file = "app_data/text.txt"
lowers_file = "app_data/lowers.txt"
longest_file = "app_data/longest.txt"
shortest_file = "app_data/shortest.txt"
words_file = "app_data/words.csv"


# перевести текст из исходного файла в нижний регистр, сохранить в файле lowers.txt
def proc01():
    print(u.green_l('1. Перевести текст из исходного файла в нижний регистр, сохранить в файле lowers.txt'))

    text = get_text(text_file)

    # вывод исходного текста
    print(u.green_l(f'Исходный текст из файла {text_file}:\n'))
    print(u.cyan(text), end='\n\n')

    # запись в файл результата обработки
    with open(lowers_file, 'w', encoding='utf-8') as file:
        file.write(text.lower())

    # вывод обработанного текста
    print(u.green_l(f'Обработанный текст в файле: "{lowers_file}"\n'))
    print(u.cyan(get_text(lowers_file)), end='\n\n')


# в файле lowers.txt подсчитать количество строк, слов, определить максимальную длину слова и список слов 
# максимальной длины, минимальную длину слова и список слов минимальной длины, сохраните списки слов в файлах 
# longest.txt и shortest.txt соответственно для слов максимальной и минимальной длины
def proc02():
    print(u.green_l('2. Статистика слов'))

    text = get_text(lowers_file)

    amount_lines = len(text.splitlines())

    words = get_words(text)

    min_length = len(min(words, key=len))

    def min_length_words_predicate(word: str):
        return len(word) == min_length

    max_length = len(max(words, key=len))

    def max_length_words_predicate(word: str):
        return len(word) == max_length

    statistic = {
        'amount_lines': amount_lines,
        'amount_words': len(words),
        'min_length': min_length,
        'min_words': words_by_length(words, min_length_words_predicate),
        'max_length': max_length,
        'max_words': words_by_length(words, max_length_words_predicate),
    }

    # сохранение статистики (списков слов) в файлы по заданию
    write_statistic_to_files(statistic)

    print(
        u.green_l(f'\tКоличество строк: {u.cyan_l(statistic["amount_lines"])}\n') +
        u.green_l(f'\tКоличество слов : {u.cyan_l(statistic["amount_words"])}\n\n') +
        u.green_l(f'\tСписок слов минимальной длины. Минимальная длина слова: {u.cyan_l(statistic["min_length"])}\n') +
        to_string_list_words(statistic['min_words']) +
        u.green_l(
            f'\tСписок слов максимальной длины. Максимальная длина слова: {u.cyan_l(statistic["max_length"])}\n') +
        to_string_list_words(statistic['max_words']) +
        u.green_l('Слова сохранены минимальной длины сохранены в '
                  f'файле "{shortest_file}", а максимальной в "{longest_file}"\n')
    )


# строка для вывода списка слов в консоль
def to_string_list_words(words: list | set):
    line = '\t'

    i = 1
    for word in words:
        line += u.cyan_l(f"{word:15}") + (' | ' if not (i % 3) == 0 else '\n\t')
        i += 1

    line += '\n'

    return line


# записать статистику слов в файлы по заданию 
# списки слов в файлах longest.txt и shortest.txt соответственно для слов максимальной и минимальной длины
def write_statistic_to_files(statistic: dict):
    write_list_to_file(statistic['max_words'], longest_file)
    write_list_to_file(statistic['min_words'], shortest_file)


# запись списка в файл
def write_list_to_file(collection: list | set, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as file:
        for item in collection:
            file.write(item + '\n')


# получить слова по заданной длине и список таких слов
def words_by_length(words: list[str], predicate):
    return set(filter(predicate, words))


# сформируйте словарь из слов файла lowers.txt – ключом является слово, значением – количество вхождений этого слова
# в текст. Сохраните этот словарь в формате CSV, имя файла words.csv
def proc03():
    print(u.green_l('3. Частотный словарь'))

    text = get_text(lowers_file)

    words = get_words(text)

    dictionary = get_frequency_dictionary(words)

    # запись в файл
    write_frequency_dictionary_to_csv_file(dictionary, words_file)

    # вывод частотного словаря
    print(to_string_dict_words(dictionary))
    print(u.green_l(f'Частотный словарь сохранён в файле: {words_file}\n\n'))


# получение частотного словаря слов
def get_frequency_dictionary(words: list):
    dictionary = dict()

    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return dictionary


# строка для вывода списка слов в консоль
def to_string_dict_words(dictionary: dict):
    line = '\t'

    i = 1
    for word in dictionary:
        line += u.cyan_l(f"{word:17}: {dictionary[word]:3}") + (' | ' if not (i % 3) == 0 else '\n\t')
        i += 1

    line += '\n'

    return line


# запись частотного словаря в csv файл
def write_frequency_dictionary_to_csv_file(dictionary: dict, file_name: str):
    with open(file_name, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for word in dictionary:
            writer.writerow([word, dictionary[word]])


# получить слова
def get_words(text: str):
    separators = '.,!?-—()[]\n\r\t'

    for s in separators:
        text = text.replace(s, ' ')

    words = text.split(' ')

    def is_not_empty(word: str):
        return len(word) > 0

    words = list(filter(is_not_empty, words))

    return words


# получить текст из файла
def get_text(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()


if __name__ == "__main__":
    from main import main

    main()
