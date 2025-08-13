# Primero se instala socket con el siguiente comando  "pip install socket"
import socket

#Escogemos la ip publica a la que le veremos el dominio junto a un puerto abierto
ippublica = input("Por favor, la direccion ip de la pagina web (ej: 8.8.8.8) : ")

ippublica_conpuerto = ("ippublica", 80)
Info = socket.getnameinfo(ippublica_conpuerto, 0) #hayamos la ip publica
print(Info) #se muestra la informacion



