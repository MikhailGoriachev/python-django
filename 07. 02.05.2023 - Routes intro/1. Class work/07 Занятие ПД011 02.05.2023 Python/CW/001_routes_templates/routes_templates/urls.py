"""
URL configuration for routes_templates project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

# подключение класса TemplateView - если по маршруту надо просто
# вывести страницу, то делать функцию в представлении необязательно
from django.views.generic import TemplateView

from routes.views import index, page1, page2, param1, param2, param3, param4
from routes.views import conditional, loop, static_files

urlpatterns = [
    # по пути вида localhost:p/ применим TemplateView
    path('', TemplateView.as_view(template_name='index.html')),

    # path(route, function, pathName, **kwargs)
    # *args    - список необязательных параметров - уточнить - имеется в каждой ф-ии
    # **kwargs - словарь необязательных параметров
    path('index/', index),
    path('page1/', page1, name='page1', kwargs={"color":"red", "number":24, "state": False}),

    # передача параметра в маршруте
    path('page2/', page2, name='page2'),
    path('page2/<str:color>/', page2, name='page2'),

    # примеры передачи параметров в маршруте
    path('param1/<int:number>/', param1),
    path('param2/<str:name>/<int:id>/', param2),
    path('param3/<slug:info>/', param3),
    path('param4/<path:data>/', param4),

    # демонстрация встроенных тегов шаблонов
    path('conditional/', conditional),
    path('loop/', loop),

    # использование static-файлов (CSS, картинки, ...)
    path('static_files/', static_files),

]
