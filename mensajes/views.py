from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Mensajes

# Create your views here.

def mensajes_recibidos(request, username):
    destinatario = get_object_or_404(User, username = username)
    mensajes = Mensajes.objects.filter(destinatario = destinatario).order_by('-fecha_de_envio')
    return render(request, 'mensajes/mensajes_recibidos.html', {'destinatario': destinatario, 'mensajes': mensajes})

