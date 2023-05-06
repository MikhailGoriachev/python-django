from django.shortcuts import render


# Переход по маршруту /index
def index(request):
    return render(request, 'index.html')


# получение параметров из urls, передача в шаблон
def page1(request, color, number, state):
    # ключи могут быть с любыми именами
    return render(request, 'page1.html', context={"color": color, "number": number, "state": state})


# передача параметров в маршруте вида localhost:p/string_color_name
# значение по умолчанию используется, если параметр не задан в запросе
def page2(request, color="undefined"):
    data = {"color": color}
    return render(request, 'page2.html', context=data)


# localhost:p/param1/<int:number>/
def param1(request, number):
    return render(request, 'param_view.html', context={"data": f"{number}"})


# localhost:p/param2/<str:name>/<int:id>/
def param2(request, name, id):
    return render(request, 'param_view.html', context={"data": f"name = {name}, id = {id}"})


# localhost:p/param3/<slug:info>/
def param3(request, info):
    return render(request, 'param_view.html', context={"data": info})


# localhost:p/param4/<path:data>/
def param4(request, data):
    return render(request, 'param_view.html', context={"data": data})


# ------------------------------------------------------------


# localhost:p/conditional
def conditional(request):
    return render(request, 'conditional.html', {"n": 42})


# localhost:p/loop
def loop(request):
    return render(request, 'loop.html', {"data": ['C++', 'UML', 'C#', 'T-SQL', 'JavaScript']})


# localhost:p/static
def static_files(request):
    return render(request, 'static_files.html', {"n": 42, "data": ['C++', 'UML', 'C#', 'T-SQL', 'JavaScript']})
