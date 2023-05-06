"""
URL configuration for test_project project.

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
# from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from first.views import index
from second.views import second_index

urlpatterns = [
    path('', index),

    # если по запросу надо просто вывести разметку
    # например, GET-запрос формы можно использовать классы
    path('index/', TemplateView.as_view(template_name='index.html')),
    path('first/', TemplateView.as_view(template_name='index.html')),
    path('second1/', TemplateView.as_view(template_name='second_index.html')),
    path('second/', second_index),
]
