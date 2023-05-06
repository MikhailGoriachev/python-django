from django.contrib import admin
from django.urls import path

from calc.views import index, euclide, about

urlpatterns = [
    path('admin/', admin.site.urls),

    # index/ – вывод страницы со списком времен года с вложенными списками –перечислениями названий месяцев времен года
    path('index/', index),

    # euclide/ - вывод страницы с именем математика Эвклида и датами его жизни
    path('euclide/', euclide),

    # about/ – сведения о разработчике
    path('about/', about),
]
