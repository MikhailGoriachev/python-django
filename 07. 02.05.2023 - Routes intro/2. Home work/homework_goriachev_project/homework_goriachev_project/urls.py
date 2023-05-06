from django.urls import path

from calc.views import index, about, sort_by, nod, insert_last, replace_first, delete_last, employee, product

urlpatterns = [

    # index/ – вывод технического задания
    path('', index),
    path('index/', index),

    # about/ – вывод сведений о разработчике
    path('about/', about),

    # sort/string/number1/number2/number3/ – в зависимости от значения строкового параметра ("ascend" или "descend") 
    # сортировка трех чисел по возрастанию или по убыванию соответственно. Не используйте агрегатные типы данных
    path('sort/<str:string>/<int:number1>/<int:number2>/<int:number3>/', sort_by),

    # nod/number1/number2/ – вычисление наибольшего общего делителя по алгоритму Евклида (примените рекурсивную 
    # реализацию алгоритма, в шаблоне выведите изображение этого самого Евклида)
    path('nod/<int:number1>/<int:number2>/', nod),

    # insertlast/string1/string2/string3/ – в строку string1 вставляет подстроку string3 после последнего вхождения 
    # подстроки string2
    path('insertlast/<str:string1>/<str:string2>/<str:string3>/', insert_last),

    # replacefirst/string1/string2/string3/ – в строке string1 заменяет первое вхождение подстроки string2 на подстроку 
    # string3
    path('replacefirst/<str:string1>/<str:string2>/<str:string3>/', replace_first),

    # delete-last/string1/string2/ – из строки string1 удаляет последнее вхождение подстроки string2
    path('delete-last/<str:string1>/<str:string2>/', delete_last),

    # employee/id/name/salary/ – выводит данные работника, в том числе и фото из статического файла 
    # (имя файла формируйте в представлении, из id)
    path('employee/<int:id>/<str:name>/<int:salary>/', employee),

    # product/id/name/quantity/price/ – выводит данные товара, в том числе и фото из статического файла 
    # (имя файла формируйте в представлении, из id)
    path('product/<int:id>/<str:name>/<int:quantity>/<int:price>', product),
]
