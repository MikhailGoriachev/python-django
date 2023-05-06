from django.shortcuts import render


# Create your views here.

# index/ – вывод страницы со списком времен года с вложенными списками –перечислениями названий месяцев времен года
def index(request):
    return render(request, 'index.html')


# euclide/ - вывод страницы с именем математика Эвклида и датами его жизни
def euclide(request):
    return render(request, 'euclide.html')


# about/ – сведения о разработчике
def about(request):
    return render(request, 'about.html')
