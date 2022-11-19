from django.urls import path
from . import views


urlpatterns = [
    path("cliente", views.clientesHome,  name="homeClientes"),
   
]