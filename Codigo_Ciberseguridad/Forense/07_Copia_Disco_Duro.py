# Este es un codigo para extraer la mayor cantidad de informacion de
# Un sistema operativo Android, como requisito hay que descargar
# El software y luego instalar las librerias de python
# Por ultimo dar los permisos adminin al archivo o terminal
# wsl --install
# pip install --user buildozer
# buildozer init
import hashlib

def copia_forense_a_iso(origen, salida_iso, tamano_bloque=4096):
    """
    Realiza una copia forense bit a bit desde un disco o partición a un archivo con extensión .iso.
    
    :param origen: Ruta al dispositivo de origen (ej. /dev/sdb o \\.\PhysicalDrive1)
    :param salida_iso: Nombre del archivo ISO destino (ej. disco.iso)
    :param tamano_bloque: Tamaño del bloque de lectura en bytes (default: 4096)
    """
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
copia_forense_a_iso(r"\\.\PhysicalDrive1", "Disco_Duro.iso")


