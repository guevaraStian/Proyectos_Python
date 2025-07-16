# Con este codigo se realiza un Escaner de bluetooth con la libreria bleak
# Con la libreria de python Scapy
# pip install bleak
import asyncio
from bleak import BleakScanner
import math
import time
import matplotlib.pyplot as plt
import random
from datetime import datetime
import os

# ----------- Calcular distancia basada en RSSI -----------
def calcular_distancia(rssi, tx_power=-59):
    if rssi == 0:
        return -1.0
    ratio = rssi / tx_power
    if ratio < 1.0:
        return ratio ** 10
    else:
        return 0.89976 * (ratio ** 7.7095) + 0.111

# ----------- Crear gráfico tipo radar -----------
def radar_visual(dispositivos_info):
    plt.figure(figsize=(7, 7))
    ax = plt.subplot(111, polar=True)
    ax.set_ylim(0, 10)
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)

    for info in dispositivos_info:
        angulo = info['angulo']
        distancia = info['distancia']
        etiqueta = f"{info['nombre'] or 'Desconocido'}\n{info['direccion']}\n{distancia:.1f}m"
        ax.plot(angulo, distancia, 'ro')  # punto rojo
        ax.text(angulo, distancia + 0.3, etiqueta, fontsize=7, ha='center')

    ax.set_title("Radar Bluetooth - Nombre, MAC y distancia", fontsize=12)
    plt.tight_layout()

    # ----------- Guardar imagen con fecha y hora -----------
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"Radar_Bluetooth_{now}.png"
    output_path = os.path.join(os.getcwd(), filename)
    plt.savefig(output_path)
    print(f"📸 Radar guardado como: {filename}")
    plt.close()

# ----------- Escaneo BLE y control del radar -----------
async def escanear_y_mostrar_radar():
    dispositivos_vistos = {}  # MAC -> ángulo

    try:
        while True:
            print(f"\n[{time.strftime('%H:%M:%S')}] Escaneando Bluetooth...")
            dispositivos = await BleakScanner.discover(timeout=5.0)
            dispositivos_info = []

            for d in dispositivos:
                if d.rssi is None:
                    continue
                distancia = calcular_distancia(d.rssi)

                if d.address not in dispositivos_vistos:
                    dispositivos_vistos[d.address] = random.uniform(0, 2 * math.pi)

                dispositivos_info.append({
                    'nombre': d.name,
                    'direccion': d.address,
                    'rssi': d.rssi,
                    'distancia': distancia,
                    'angulo': dispositivos_vistos[d.address]
                })

            if dispositivos_info:
                radar_visual(dispositivos_info)
            else:
                print("⚠️  No se detectaron dispositivos BLE.")
            
            await asyncio.sleep(10)  # espera antes del siguiente escaneo

    except KeyboardInterrupt:
        print("🚫 Escaneo detenido por el usuario.")

# ----------- MAIN -----------
if __name__ == "__main__":
    asyncio.run(escanear_y_mostrar_radar())