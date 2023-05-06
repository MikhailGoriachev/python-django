from datetime import datetime
from django.shortcuts import render


# маршрут localhost:p/, localhost:p/index
def index(request):
    return render(request, 'index.html', context={"date_now": datetime.now()})
# end index


# маршрут localhost:p/complex_example/<int:number>
def complex_example(request, number=24):
    data = ['C++', 'Java', 'JavaScript', 'C#', 'PHP', 'Python', 'TypeScript']

    return render(request, 'complex_example.html', context={"number": number, "data":data})
# end complex_example


# маршрут с параметрами строки запроса
# localhost:p/query_params/
def query_params(request):

    # получение параметров из строки запроса - параметры GET-запроса
    # get(имяПараметра) или get(имяПараметра, значениеПоУмолчанию)
    id=request.GET.get('id', 0)
    name=request.GET.get('name', 'undefined')
    price=request.GET.get('price', '0')
    amount=request.GET.get('amount', '0')
    product = {"id":id, "name":name, "price":price, "amount":amount}

    return render(request, 'query_params.html', context={"product": product})
# end query_params


# маршрут вывода формы
def get_user_form(request):
    return render(request, 'user_form.html')
# end get_user_form


# обработчик POST-запроса от формы, вывод данных на страницу user_view.html
def post_user_form(request):
    # получаем данные из формы
    full_name = request.POST.get("fullName", "не определено")
    weight = request.POST.get("weigth", 0)
    height = request.POST.get("height", 0)

    # чтение значения из группы радиокнопок - просто значение переменной
    # для удобства перекодировки применим словарь
    # т.к. словарь нужен только один раз зададим словарь литералом
    transport = request.POST.get("transport", 'none')
    transport = {
        'communal':'общественный',
        'car':'автомобиль',
        'taxi':'такси',
        'motorcycle':'мотоцикл',
        'bicycle':'велосипед',
        'none':'не указан',
        }[transport]

    # получение значений чек-боксов (логические значения)
    library = request.POST.get('library', False)
    gym = request.POST.get('gym', False)
    swim_pool = request.POST.get('swim_pool')

    # для удобства рендеринга применим словарь
    user = {
        "full_name": full_name,
        "weight": weight,
        "height": height,
        "transport": transport,
        "library": library,
        "gym": gym,
        "swim_pool": swim_pool,
    }

    return render(request, 'user_view.html', context={"user": user})
# end post_user_form
