from django.urls import path
from . import views


urlpatterns = [
    path("cliente", views.clientesHome,  name="homeClientes"),
    path("cliente-registro", views.clientesRegistro,  name="registroClientes"),
    path("cliente-peticiones", views.clientesPeticiones,  name="peticionesClientes"),
    path("cliente-peticiones-hechas", views.clientesPeticionesHechas,  name="peticionesHechasClientes"),
    path("repartidor", views.repartidorHome,  name="homeRepartidor"),
    path("repartidor-registro", views.repartidorRegistro,  name="registroRepartidor"),
    path("repartidor-peticiones", views.repartidorPeticiones,  name="peticionesRepartidor"),
]