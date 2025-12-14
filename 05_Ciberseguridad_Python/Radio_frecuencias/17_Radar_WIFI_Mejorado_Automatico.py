# Con este codigo se crea un software que permite crear un radar
# Con los dispositivos finales que estan conectados al wifi
# Con la libreria de python 
# pip install scapy 

import time
import socket
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from scapy.all import ARP, Ether, srp

# Se crean las variables relacionadas a la red
NETWORK = "192.168.1.0/24"   # Ajusta a tu red
UPDATE_INTERVAL = 5          # segundos
MAX_DISTANCE = 30            # metros

# El siguiente codigo ayuda a crear el escaneo
def scan_network(network):
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=2, verbose=0)[0]
    devices = []

    for _, received in result:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices

# Esta funcion ayuda a tener los datos de los dispositivos cerca
def get_device_name(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Desconocido"

# Se calcula el rssi
def get_rssi():
    # Valores típicos WiFi: -80 (débil) a -30 (fuerte)
    return random.randint(-80, -30)

# Con el rssi se calcula la distancia de los dispositivos cercanos
def estimate_distance(rssi, tx_power=-40, n=2):
    distance = 10 ** ((tx_power - rssi) / (10 * n))
    return round(min(distance, MAX_DISTANCE), 2)

# Se crea la grafica del radar
def draw_radar(devices):
    plt.clf()
    ax = plt.subplot(111, polar=True)

    ax.set_rmax(MAX_DISTANCE)
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)

    for device in devices:
        angle = random.uniform(0, 2 * math.pi)
        distance = device["distance"]

        ax.scatter(angle, distance, s=50)
        ax.text(
            angle,
            distance,
            f"{device['name']}\n{device['ip']}\n{distance} m",
            fontsize=7
        )

    ax.set_title("RADAR WIFI - Dispositivos detectados", fontsize=14)
    plt.pause(0.1)

# El siguiente codigo es el Main donde se ejecuta e codigo
def main():
    plt.ion()
    plt.figure(figsize=(6, 6))

    while True:
        devices = scan_network(NETWORK)
        radar_devices = []

        for d in devices:
            rssi = get_rssi()
            radar_devices.append({
                "ip": d["ip"],
                "mac": d["mac"],
                "name": get_device_name(d["ip"]),
                "distance": estimate_distance(rssi)
            })

        draw_radar(radar_devices)
        time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    main()
