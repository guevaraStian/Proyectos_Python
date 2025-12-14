# Con este codigo se crea un software que muestra 
# Listado de los dispositivos finales conectados al wifi
# Con la libreria de python 
# pip install scapy 

import time
import socket
import requests
from scapy.all import ARP, Ether, srp
from datetime import datetime

# Variables de red
NETWORK = "192.168.1.0/24"   # La red donde estas
SCAN_INTERVAL = 10           # segundos entre escaneos
known_devices = {}

# Funcion de recolectar informacion

def scan_network():
    devices = {}
    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=NETWORK)
    result = srp(packet, timeout=3, verbose=False)[0]

    for _, received in result:
        devices[received.hwsrc] = received.psrc

    return devices


def get_mac_vendor(mac):
    try:
        r = requests.get(
            f"https://api.macvendors.com/{mac}",
            timeout=3
        )
        if r.status_code == 200:
            return r.text.strip()
    except:
        pass
    return "Desconocido"


def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "No disponible"


# Codigo para mostrar la informacion

def show_all_devices(devices):
    print("\n DISPOSITIVOS CONECTADOS A LA RED")
    print("=" * 80)

    for mac, ip in devices.items():
        print(f"IP        : {ip}")
        print(f"MAC       : {mac}")
        print(f"Fabricante: {get_mac_vendor(mac)}")
        print(f"Hostname  : {get_hostname(ip)}")
        print("-" * 80)

# En el siguiente codigo se muestra como detectar un nuevo dispositvo conectado
def alert_new_device(mac, ip):
    print("\n!! NUEVO DISPOSITIVO DETECTADO !!")
    print(f"Fecha/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"IP        : {ip}")
    print(f"MAC       : {mac}")
    print(f"Fabricante: {get_mac_vendor(mac)}")
    print(f"Hostname  : {get_hostname(ip)}")
    print("Estado    : NUEVA CONEXIÓN")
    print("=" * 80)


# Codigo el monitoreo de la red

def monitor_network():
    global known_devices

    print("Monitor de red Wi‑Fi iniciado...")
    print(f"Rango de red: {NETWORK}")
    print(f"Intervalo de escaneo: {SCAN_INTERVAL} segundos\n")

    while True:
        current_devices = scan_network()

        # Mostrar listado completo
        show_all_devices(current_devices)

        # Detectar nuevos dispositivos
        for mac, ip in current_devices.items():
            if mac not in known_devices:
                alert_new_device(mac, ip)

        known_devices = current_devices
        time.sleep(SCAN_INTERVAL)


# Main que ejecuta el monitoreo

if __name__ == "__main__":
    monitor_network()
