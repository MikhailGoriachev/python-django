from django.shortcuts import render


# localhost:p/second
def second_index(request):
    return render(request, 'second_index.html')

