# Primero se instala socket con el siguiente comando  "pip install socket"
#Primero se instala platform con el siguiente comando  "pip install platform"
import socket
import platform

url_victima = input("Por favor, la direccion url o ip de la pagina web (ej: 8.8.8.8) : ")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((url_victima, 80))

print(s.getsockname()[0]) #Muestra en pantalla la IP privada del computador donde se ejecuta
print(socket.gethostname()) #Muestra en pantalla el hostnme del computador donde se ejecuta
print (platform.node()) #Muestra en pantalla el hostnme del computador donde se ejecuta

