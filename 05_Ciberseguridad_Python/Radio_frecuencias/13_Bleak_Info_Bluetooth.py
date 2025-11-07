# Con este codigo se crea un software que saca informacion de Bluetooth
# Con la libreria de python bleak
# pip install pybluez bleak
import asyncio
from bleak import BleakScanner, BleakClient

async def conectar_y_extraer_info():
    print("Escaneando dispositivos Bluetooth...")
    dispositivos = await BleakScanner.discover(timeout=5.0)

    if not dispositivos:
        print("No se detectaron dispositivos.")
        return

    # Mostramos dispositivos
    for i, d in enumerate(dispositivos):
        print(f"[{i}] {d.name or 'Desconocido'} | {d.address} | RSSI: {d.rssi} dBm")

    # Selecciona uno
    indice = int(input("Selecciona el índice del dispositivo a conectar: "))
    device = dispositivos[indice]

    print(f"Conectando a {device.name or 'Desconocido'} ({device.address})...")

    async with BleakClient(device.address) as client:
        print("Conectado.")

        # Listar servicios y características disponibles
        for service in client.services:
            print(f"\n📡 Servicio: {service.uuid}")
            for char in service.characteristics:
                props = ', '.join(char.properties)
                print(f" - Característica: {char.uuid} ({props})")
                # Si es legible, intentamos leer
                if "read" in char.properties:
                    try:
                        value = await client.read_gatt_char(char.uuid)
                        print(f"Valor leído: {value}")
                    except Exception as e:
                        print(f"Error al leer: {e}")

if __name__ == "__main__":
    asyncio.run(conectar_y_extraer_info())