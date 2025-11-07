# Con este codigo se realiza un IDS detector de GPS cercanos
# Con la libreria de python Scapy
# pip install pybluez bleak
import asyncio
from bleak import BleakScanner
import math
import time
import matplotlib.pyplot as plt
import random
from datetime import datetime
import os

def calcular_distancia(rssi, tx_power=-59):
    if rssi == 0:
        return -1.0
    ratio = rssi / tx_power
    if ratio < 1.0:
        return pow(ratio, 10)
    else:
        return 0.89976 * pow(ratio, 7.7095) + 0.111

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
        ax.plot(angulo, distancia, 'go')  # punto verde
        ax.text(angulo, distancia + 0.4, etiqueta, fontsize=8, ha='center')

    ax.set_title("📡 Radar de Dispositivos GPS (BLE cercanos)", fontsize=13)
    plt.tight_layout()

    # Guardar imagen con fecha y hora
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"gps_radar_{now}.png"
    output_path = os.path.join(os.getcwd(), filename)
    plt.savefig(output_path)
    print(f"✅ Imagen guardada como: {filename}")
    plt.close()

async def escanear_y_radar():
    dispositivos_vistos = {}

    try:
        while True:
            print(f"\n[{time.strftime('%H:%M:%S')}] Escaneando dispositivos GPS...")
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
                print("⚠️  No se detectaron dispositivos BLE cercanos.")
            
            await asyncio.sleep(10)  # escanea cada 10 segundos

    except KeyboardInterrupt:
        print("🛑 Escaneo detenido por el usuario.")

if __name__ == "__main__":
    asyncio.run(escanear_y_radar())




    