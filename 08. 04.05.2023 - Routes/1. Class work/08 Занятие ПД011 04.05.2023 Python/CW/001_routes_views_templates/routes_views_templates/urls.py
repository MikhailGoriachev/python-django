from django.urls import path
from app_first import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index, name='home'),

    path('complex_example/', views.complex_example),
    path('complex_example/<int:number>/', views.complex_example, name='complex_example'),

    # передача параметров через строку запроса
    path('query_params/', views.query_params),

    # вывод страницы с формой
    path('get_user_form/', views.get_user_form),

    # обработка формы
    path('post_user_form/', views.post_user_form),
]
