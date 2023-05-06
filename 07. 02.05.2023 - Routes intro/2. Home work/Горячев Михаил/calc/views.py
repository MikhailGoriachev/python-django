from django.shortcuts import render


# index/ – вывод технического задания
def index(request):
    return render(request, 'index.html')


# about/ – вывод сведений о разработчике
def about(request):
    return render(request, 'about.html')


# sort/string/number1/number2/number3/ – в зависимости от значения строкового параметра ("ascend" или "descend") 
# сортировка трех чисел по возрастанию или по убыванию соответственно. Не используйте агрегатные типы данных
def sort_by(request, string: str, number1: int, number2: int, number3: int):
    number1_old, number2_old, number3_old = number1, number2, number3

    sort_type, comparator = ('по возрастанию', lambda a, b: a < b) if string == 'ascend' \
        else ('по убыванию', lambda a, b: a > b)

    # сортировка по компаратору
    if not comparator(number1, number2):
        number1, number2 = number2, number1
    if not comparator(number1, number3):
        number1, number3 = number3, number1
    if not comparator(number2, number3):
        number2, number3 = number3, number2

    return render(request, 'sort.html', {
        'sort_type': sort_type,
        'number1': number1, 'number2': number2, 'number3': number3,
        'number1_old': number1_old, 'number2_old': number2_old, 'number3_old': number3_old
    })


# nod/number1/number2/ – вычисление наибольшего общего делителя по алгоритму Евклида (примените рекурсивную 
# реализацию алгоритма, в шаблоне выведите изображение этого самого Евклида)
def nod(request, number1: int, number2: int):
    # получение НОД
    def get_gcd(a: int, b: int):
        return a if b == 0 else get_gcd(b, a % b)

    gcd = get_gcd(number1, number2)

    return render(request, 'nod.html', {'number1': number1, 'number2': number2, 'gcd': gcd})


# insertlast/string1/string2/string3/ – в строку string1 вставляет подстроку string3 
# после последнего вхождения подстроки string2
def insert_last(request, string1: str, string2: str, string3: str):
    insert_index = string1.rindex(string2) + len(string2)
    result = f'{string1[:insert_index]}{string3}{string1[insert_index:]}'

    return render(request, 'insert_last.html', {
        'string1': string1, 'string2': string2, 'string3': string3, 'result': result
    })


# replacefirst/string1/string2/string3/ – в строке string1 заменяет первое вхождение подстроки string2 
# на подстроку string3
def replace_first(request, string1: str, string2: str, string3: str):
    result = string1.replace(string2, string3, 1)

    return render(request, 'replace_first.html', {
        'string1': string1, 'string2': string2, 'string3': string3, 'result': result
    })


# delete-last/string1/string2/ – из строки string1 удаляет последнее вхождение подстроки string2
def delete_last(request, string1: str, string2: str):
    result = ''.join(string1.rsplit(string2, 1))

    return render(request, 'delete_last.html', {
        'string1': string1, 'string2': string2, 'result': result
    })


# employee/id/name/salary/ – выводит данные работника, в том числе и фото из статического файла (имя файла формируйте
# в представлении, из id)
def employee(request, id: int, name: str, salary: int):
    image = f'images/employee_{f"{id:>2}".replace(" ", "0")}.jpg'
    return render(request, 'employee.html', {'id': id, 'name': name, 'salary': salary, 'image': image})


# product/id/name/quantity/price/ – выводит данные товара, в том числе и фото из статического файла (имя файла 
# формируйте в представлении, из id)
def product(request, id: int, name: str, quantity: int, price: int):
    image = f'images/product_{f"{id:>2}".replace(" ", "0")}.png'
    return render(request, 'product.html', {
        'id': id, 'name': name, 'quantity': quantity, 'price': price, 'image': image
    })
