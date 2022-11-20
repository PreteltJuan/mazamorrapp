from django.urls import path
from . import views


urlpatterns = [
    path("home", views.clientesHome,  name="home"),
    path("restaurante/<nombre_r>", views.restaurante,  name="restaurante")
    
]