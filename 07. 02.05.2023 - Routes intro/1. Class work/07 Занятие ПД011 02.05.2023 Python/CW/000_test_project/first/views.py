from django.shortcuts import render


# маршурт localhost:p/
def index(request):
    return render(request, 'index.html')
