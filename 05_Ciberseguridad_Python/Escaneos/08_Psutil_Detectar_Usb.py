# Con este codigo se crea un detectador de USB
# Usando la libreria Psutil
# pip install pywin32 psutil
import psutil
import time
import subprocess

# Con esta funcion se logran inicializar la libreria psulti y darle las caracteristicas
def get_usb_drives():
    drives = []
    partitions = psutil.disk_partitions(all=False)
    for p in partitions:
        if 'removable' in p.opts or 'cdrom' in p.opts:
            drives.append(p.device)
    return set(drives)

print("Monitoreando conexiones USB...")
previous = get_usb_drives()

# Se deja escuchando los puertos usb y se crea un while
# Con el fin de que se ejecute cada que ingrese una usb a los puertos
while True:
    time.sleep(2)
    current = get_usb_drives()
    new_devices = current - previous

    if new_devices:
        for device in new_devices:
            print(f"Nueva USB detectada: {device}")
            # Aquí puedes ejecutar cualquier script o acción
            #subprocess.run(["python", "tu_script.py"])  # Cambia por tu ruta
    previous = current

