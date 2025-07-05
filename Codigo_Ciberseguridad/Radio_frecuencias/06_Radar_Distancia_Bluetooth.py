# En este ejemplo de codigo se muestra la creacion de un radar
# con la distancia de los dispositivos cerca al bluetooth
# pip install bleak matplotlib
import asyncio
from bleak import BleakScanner
import math
import random
import matplotlib.pyplot as plt

# Se crea la logica de calcular la distancia rssi del dron
def estimar_distancia(rssi, tx_power=-59, n=2.0):
    if rssi == 0:
        return None
    return round(10 ** ((tx_power - rssi) / (10 * n)), 2)

# En la siguiente funcion se crea la imagen del radar con la distancia probable
def mostrar_radar(dispositivos_info):
    fig, ax = plt.subplots()
    ax.set_title("Radar Bluetooth - Distancia estimada por RSSI")
    ax.set_xlim(-12, 12)
    ax.set_ylim(-12, 12)
    ax.set_aspect('equal')
    ax.grid(True)
    
    # En el siguiente codigo se ingresan los datos de distancia a la grafica
    for nombre, mac, distancia in dispositivos_info:
        if distancia is None or distancia > 20:
            continue
        angle = random.uniform(0, 2 * math.pi)
        x = distancia * math.cos(angle)
        y = distancia * math.sin(angle)
        ax.plot(x, y, 'go')
        ax.text(x, y, f"{nombre or mac}\n{distancia} m", fontsize=8)

    plt.show()

# En la siguiente funcion se ejecuta la escaneada de bluetooth
async def escanear_dispositivos():
    print("🔍 Escaneando dispositivos Bluetooth (BLE)...")
    dispositivos_info = []
    devices = await BleakScanner.discover(timeout=10)

    for d in devices:
        nombre = d.name or "Desconocido"
        mac = d.address
        rssi = d.rssi
        distancia = estimar_distancia(rssi)
        dispositivos_info.append((nombre, mac, distancia))
        print(f"📡 {nombre} ({mac}) - RSSI: {rssi} dBm -> Distancia estimada: {distancia} m")

    return dispositivos_info

# En el main se ejecutan las funciones y si no hay dispositivos se muestra un mensaje

def main():
    dispositivos_info = asyncio.run(escanear_dispositivos())
    if dispositivos_info:
        mostrar_radar(dispositivos_info)
    else:
        print("No se detectaron dispositivos BLE.")

if __name__ == "__main__":
    main()







