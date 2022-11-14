from django.urls import path
from . import views


urlpatterns = [
    path("cliente", views.clientesHome,  name="homeClientes"),
    path("vendedor", views.vendedoresHome,  name="homeVendedores"),
   
]