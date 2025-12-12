# Con este codigo se crea un software que permite enviar
# Informacion por medio de bloutu a dispositivos cercanos
# Con la libreria de python 
# pip install bleak
import asyncio
from bleak import BleakScanner, BleakClient

# UUID de la característica BLE donde escribirás texto:
WRITE_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"   # <-- reemplaza esto

async def main():
    print("Escaneando dispositivos Bluetooth...")
    devices = await BleakScanner.discover(timeout=5.0)

    if not devices:
        print("No se encontraron dispositivos.")
        return

    # Mostrar lista con índices
    for idx, dev in enumerate(devices, start=1):
        print(f"{idx}. {dev.name}  [{dev.address}]")

    # Elegir dispositivo
    num = int(input("\nSelecciona el dispositivo por índice: "))
    device = devices[num - 1]

    print(f"\nConectando a {device.name} ({device.address})...")

    async with BleakClient(device.address) as client:
        if not client.is_connected:
            print("Error: no se pudo conectar.")
            return
        
        print("Conectado!")

        # Pedir texto
        msg = input("Escribe el texto a enviar: ")

        # Convertir a bytes
        data = msg.encode("utf-8")

        # Enviar
        await client.write_gatt_char(WRITE_UUID, data)
        print("Texto enviado correctamente.")

asyncio.run(main())
