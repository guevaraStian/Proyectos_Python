# Primero se instala socket con el siguiente comando  "pip install socket"
import socket

#Escogemos la ip publica a la que le veremos el dominio junto a un puerto abierto
ippublica = ("8.8.8.8", 80)
Info = socket.getnameinfo(ippublica, 0) #hayamos la ip publica
print(Info) #se muestra la informacion



