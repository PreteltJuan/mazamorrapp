from django.shortcuts import render, redirect

# Create your views here.

def clientesHome(request):
    return redirect('registroClientes')

def clientesRegistro(request):
    return render(request, "pages/clienteAppRegistro.html")

def clientesPeticiones(request):
    return render(request, "pages/clienteAppPeticiones.html")


def clientesPeticionesHechas(request):
    return render(request, "pages/clienteAppPeticionesHechas.html")


def repartidorHome(request):
    return redirect('registroRepartidor')
    
def repartidorRegistro(request):
    return render(request, "pages/repartidorAppRegistro.html")

def repartidorPeticiones(request):
    return render(request, "pages/repartidorAppPeticiones.html")