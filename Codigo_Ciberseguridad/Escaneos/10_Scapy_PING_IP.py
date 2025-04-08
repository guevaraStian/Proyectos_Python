from scapy.all import IP, ICMP, sr1
import time

# Se crea la funcion que realiza el ping a una destino ip
# De las variables que tiene, se le habilita una de ip destino
def PingAUnaIp(Ip_destino, count=4, timeout=2):
    # Se crea un for que recorre las veces que le indiquemos en el count
    for i in range(count):
        # Usamos las funciones de IP e ICMP para guardar su respuesta en paquete
        Paquete = IP(dst=Ip_destino) / ICMP() 
        # Guardamos el tiempo inicial en una variable
        Tiempo_comienzo = time.time()
        # Guardamos la respuesta de sr1 con datos ya establecidos
        respuesta = sr1(Paquete, timeout=timeout, verbose=False)
        # Ponemos la condicional a esa respuesta 
        if respuesta:
            round_trip_time = (time.time() - Tiempo_comienzo) * 1000
            print(f"Ping a la IP {Ip_destino}: Respuesta lograda! TTL={respuesta.ttl} Tid={round_trip_time:.2f}ms")
        else:
            print(f"Ping a la IP {Ip_destino}: No hubo respuesta.")

if __name__ == "__main__":
    Ip_destino_ping = input("Por favor ingrese la IP destino, del ping: ")
    PingAUnaIp(Ip_destino_ping)