from django.shortcuts import render


# маршрут localhost:p/basket
def basket(request):
    return render(request, 'basket.html')
    
    
# маршрут localhost:p/order
def order(request):
     return render(request, 'order.html')

     
# маршрут localhost:p/delivery
def delivery(request):
     return render(request, 'delivery.html')  
