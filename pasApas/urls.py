from django.urls import path
from . import views

urlpatterns = [
    path('guardar', views.guardar_sesion, name='guardar-sesion'),
    path('recuperar', views.recuperar_sesion, name='recuperar-sesion')
]