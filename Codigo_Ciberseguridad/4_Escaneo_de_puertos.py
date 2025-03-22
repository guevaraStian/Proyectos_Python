# Primero se instala socket con el siguiente comando  "pip install socket"
import socket

def escanear_puerto(ip, puerto):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        resultado = sock.connect_ex((ip, puerto))
        if resultado == 0:
            print(f"Puerto {puerto} abierto en {ip}")
        sock.close()
    except socket.error:
        print(f"Error al escanear el puero {puerto} en {ip}")

ip_destino= "localhost"
puertos = [80, 443, 22, 3389]

for puerto in puertos:
    escanear_puerto(ip_destino, puerto)

