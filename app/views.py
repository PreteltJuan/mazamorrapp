from django.shortcuts import render, redirect
from .forms import OrderRequest
from .models import Order
def clientesHome(request):
    orderRequest = OrderRequest()
    return render(request, 'pages/clienteHome.html', { 'orderRequest' : orderRequest})
    

def vendedoresHome(request):
    orders = Order.objects.all()
    return render(request, 'pages/vendedorHome.html', { 'orders' : orders})
    







    