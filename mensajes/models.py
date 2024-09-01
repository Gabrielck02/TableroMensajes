from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mensajes(models.Model):
    texto_del_mensaje = models.TextField()
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "mensajes_enviados", verbose_name= "remitente")
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "mensajes_recibidos", verbose_name= "destinatario")
    fecha_de_envio = models.DateTimeField("Fecha y hora de envio ", auto_now_add= True)

def __str__(self):
    return f'Mensaje de {self.remitente.username} a {self.destinatario.username}'
