from django.contrib.auth.models import User
from mensajes.models import Mensajes

def crear_datos_de_prueba():
    # Crear usuarios de prueba
    usuario1 = User.objects.create_user(username='usuario1', password='1234')
    usuario2 = User.objects.create_user(username='usuario2', password='2345')
    usuario3 = User.objects.create_user(username='usuario3', password='3456')

    # Antes de crear un mensaje hay que obtener los usuarios que van a enviar y recibir el mensaje
    
    #remitente = User.objects.get(username='usuario1')
    
    #destinatario = User.objects.get(username='usuario2')

    # Crear mensajes de prueba
    Mensajes.objects.create(
        texto_del_mensaje='Hola, ¿cómo estás?',
        remitente=usuario1,
        destinatario=usuario2
    )
    Mensajes.objects.create(
        texto_del_mensaje='Todo bien, gracias ¿Y vos?',
        remitente=usuario2,
        destinatario=usuario1
    )
    Mensajes.objects.create(
        texto_del_mensaje='Hola buen dia, ¿Llego el mensaje?',
        remitente=usuario1,
        destinatario=usuario3
    )
    Mensajes.objects.create(
        texto_del_mensaje='Hola, si me llego el mensaje',
        remitente=usuario3,        
        destinatario=usuario1
    )

    print("Datos de prueba creados con éxito")

if __name__ == '__main__':
    crear_datos_de_prueba()