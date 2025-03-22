# Primero se instala re con el siguiente comando  "pip install re"
#Primero se instala random con el siguiente comando  "pip install random"
import re
import random

def obtener_respuesta(mensaje_del_usuario):
    mensaje_dividido = re.split(r'\s|[,:;.?!-_]\s*', mensaje_del_usuario.lower())
    respuesta = validar_todo_mensajes(mensaje_dividido)
    return respuesta

def mensaje_probabilidad(mensaje_usuario, palabras_reconocidas, respuesta_simple=False, palabra_requerida=[]):
    mensaje_requerido = 0
    palabra_requeridas = True

    for palabra in mensaje_usuario:
        if palabra in palabras_reconocidas:
            mensaje_requerido +=1

    porcentaje = float(mensaje_requerido) / float (len(palabras_reconocidas))

    for palabra in palabra_requerida:
        if palabra not in mensaje_usuario:
            palabra_requeridas = False
            break
    if palabra_requeridas or respuesta_simple:
        return int(porcentaje * 100)
    else:
        return 0

def validar_todo_mensajes(mensaje):
        alta_probabilidad = {}

        def respuesta(bot_respuesta, lista_de_palabras, respuesta_simple = False, palabra_requeridas = []):
            nonlocal alta_probabilidad
            alta_probabilidad[bot_respuesta] = mensaje_probabilidad(mensaje, lista_de_palabras, respuesta_simple, palabra_requeridas)

        respuesta('Hola', ['hola', 'hi', 'saludos', 'buenas'], respuesta_simple = True)
        respuesta('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], palabra_requeridas=['como'])
        respuesta('Estamos ubicados en la carrera 70 con calle 5', ['ubicados', 'direccion', 'donde', 'ubicacion'], respuesta_simple=True)
        respuesta('En esta empresa vendemos de todo un poquito', ['que', 'what', 'q', 'qu', 'vende', 'venta'], respuesta_simple=True)
        respuesta('Trabajamos 24 horas al dia', ['cuando', 'pueden', 'trabajan'], respuesta_simple=True)
        respuesta('Nosotros somos la empresa mas grande de colombia', ['quienes', 'quien', 'son'], respuesta_simple=True)
        respuesta('Siempre a la orden, cuando quiera nos podemos comunicar', ['gracias', 'te lo agradezco', 'thanks'], respuesta_simple=True)
        mejor_opcion = max(alta_probabilidad, key=alta_probabilidad.get)

        return desconocido() if alta_probabilidad[mejor_opcion] < 1 else mejor_opcion

def desconocido():
    respuesta = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'buscalo en google a ver que tal'][random.randrange(3)]
    return respuesta

while True:
    print("Bot: " + obtener_respuesta(input('Tu: ')))