# Primero se instala socket con el siguiente comando  "pip install socket"
import socket

#Escogemos el dominio al que le vamos a ver la ip
dominio = input("Por favor, la direccion url o ip de la pagina web (ej: www.google.com) : ")

# dominio = 'www.google.com'
print (dominio) #mostramos el nombre del dominio
print (socket.gethostbyname(dominio)) #mostramos la ip publica del dominio




