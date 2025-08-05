# Este es un codigo para extraer la mayor cantidad de informacion de
# Un sistema operativo MAC, como requisito hay que descargar
# El software y luego instalar las librerias de python
# Por ultimo dar los permisos adminin al archivo o terminal
# pip install psutil wmi
import os
import subprocess
import socket
from datetime import datetime

# Crear nombre de carpeta dinámico
hostname = socket.gethostname()
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = f"Info_Mac_{hostname}_{timestamp}"
os.makedirs(output_dir, exist_ok=True)

def save_output(name, command):
    path = os.path.join(output_dir, f"{name}.txt")
    try:
        print(f"[+] Ejecutando: {command}")
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(result.stdout.strip())
    except Exception as e:
        with open(path, "w") as f:
            f.write(f"Error ejecutando {command}:\n{e}")

# Información del sistema
save_output("sistema", "system_profiler SPSoftwareDataType")
save_output("hardware", "system_profiler SPHardwareDataType")
save_output("almacenamiento", "system_profiler SPStorageDataType")
save_output("discos", "diskutil list")
save_output("smart_status", "diskutil info disk0")

# Red
save_output("interfaces_red", "ifconfig")
save_output("rutas", "netstat -rn")
save_output("dns", "scutil --dns")
save_output("puertos_abiertos", "lsof -nP -iTCP -sTCP:LISTEN")

# CPU y RAM
save_output("cpu", "sysctl -n machdep.cpu.brand_string")
save_output("ram", "sysctl hw.memsize")

# Usuarios y grupos
save_output("usuarios", "dscl . list /Users")
save_output("grupos", "dscl . list /Groups")
save_output("usuarios_activos", "who")
save_output("sudoers", "cat /etc/sudoers")

# Procesos y servicios
save_output("procesos", "ps aux")
save_output("servicios", "launchctl list")

# Aplicaciones
save_output("aplicaciones", "ls /Applications")
save_output("paquetes_brew", "brew list")
save_output("paquetes_mas", "mas list")

# Variables de entorno
save_output("entorno", "printenv")

# Dispositivos conectados
save_output("usb", "system_profiler SPUSBDataType")
save_output("thunderbolt", "system_profiler SPThunderboltDataType")
save_output("bluetooth", "system_profiler SPBluetoothDataType")

# Logs
save_output("log_sistema", "log show --predicate 'eventMessage contains \"error\"' --last 1h")
save_output("dmesg", "dmesg | tail -n 100")

print(f"\n✅ Toda la información fue guardada en la carpeta: {output_dir}")