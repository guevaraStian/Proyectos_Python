# Este es un codigo para sacar una copia de un disco duro
# Un sistema operativo Windows 
# El software y luego instalar las librerias de python
# Por ultimo dar los permisos adminin al archivo o terminal
# pip install hashlib requests
import hashlib
import time
from datetime import datetime
import requests

Tiempo_Inicial = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
respuesta = requests.get("https://ipinfo.io/json")
datos = respuesta.json()

print("(+) Ubicación aproximada:")
print(f"IP: {datos.get('ip')}")
print(f"Ciudad: {datos.get('city')}")
print(f"Región: {datos.get('region')}")
print(f"País: {datos.get('country')}")
print(f"Ubicación (lat,long): {datos.get('loc')}")
print(f"Organización: {datos.get('org')}")
print(f"Zona Horaria: {datos.get('timezone')}")
Ubicacion = datos.get('loc')

# Con la siguiente funcion se copia la informacion en el disco duro seleccionado
def copia_forense_a_iso(origen, salida_iso, tamano_bloque=4096):
    try:
        hash_sha256 = hashlib.sha256()
        total_bytes = 0

        with open(origen, 'rb') as disco_origen, open(salida_iso, 'wb') as archivo_iso:
            print(f"Iniciando copia forense desde {origen} a {salida_iso}...")
            while True:
                bloque = disco_origen.read(tamano_bloque)
                if not bloque:
                    break
                archivo_iso.write(bloque)
                hash_sha256.update(bloque)
                total_bytes += len(bloque)
                print(f"\rCopiados {total_bytes} bytes...", end='', flush=True)

        print("\nCopia finalizada.")
        print(f"Hash SHA256 de la imagen: {hash_sha256.hexdigest()}")

    except PermissionError:
        print("Permiso denegado. Ejecuta este script como administrador o root.")
    except FileNotFoundError:
        print("Dispositivo o archivo no encontrado.")
    except Exception as e:
        print(f"Error durante la copia: {e}")

# Ejemplo de uso:
# En Linux: copia_forense_a_iso("/dev/sdb", "imagen_forense.iso")
copia_forense_a_iso(r"\\.\PhysicalDrive1", "Disco_Duro_{Tiempo_Inicial}_{Ubicacion}.iso")


