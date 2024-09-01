from django.urls import path
from . import views

urlpatterns = [
    path('mensajes/recibidos/<str:username>/', views.mensajes_recibidos, name= 'mensajes_recibidos'),    
]    