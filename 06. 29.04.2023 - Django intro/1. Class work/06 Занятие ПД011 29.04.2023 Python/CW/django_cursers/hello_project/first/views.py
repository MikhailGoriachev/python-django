from django.shortcuts import render
from django.http import HttpResponse


# маршрут localhost:p/
def hello(request):
    return HttpResponse('<h1>Привет, мир Django</h1><h2>Первое приложение</h2>')


# маршрут localhost:p/index
def index(request):
    return render(request, 'index.html')


# маршрут localhost:p/about
def about(request):
    return render(request, 'about.html')
