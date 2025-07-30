
# Este es un codigo para extraer la mayor cantidad de informacion de
# Un sistema operativo windows, como requisito hay que descargar
# El software y luego instalar las librerias de python
# Por ultimo dar los permisos adminin al archivo o terminal
# pip install psutil wmi


import os
import platform
import socket
import subprocess
import psutil
import wmi
from datetime import datetime
import getpass

# Crear carpeta con nombre basado en hostname y fecha
hostname = socket.gethostname()
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_dir = f"Info_Windows_{hostname}_{timestamp}"
os.makedirs(output_dir, exist_ok=True)

# Se guarda un archvio en la carpeta creada
def save_output(filename, content):
    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)

def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True, stderr=subprocess.DEVNULL)
        return output.strip()
    except Exception as e:
        return f"Error ejecutando comando: {command}\n{e}"

# Obtener la informacion del sistema
def get_system_info():
    return f"""\
Nombre del equipo: {hostname}
Usuario actual: {getpass.getuser()}
Sistema operativo: {platform.system()} {platform.release()}
Versión: {platform.version()}
Arquitectura: {platform.machine()}
Procesador: {platform.processor()}
"""

# Obtener la informacion del cpu
def get_cpu_info():
    return f"""\
CPUs físicos: {psutil.cpu_count(logical=False)}
CPUs lógicos: {psutil.cpu_count(logical=True)}
Uso por núcleo (%): {psutil.cpu_percent(percpu=True, interval=1)}
"""
# Obtener Informacion de la memoria volatil
def get_memory_info():
    mem = psutil.virtual_memory()
    return f"""\
Memoria total: {mem.total // (1024 ** 2)} MB
Disponible: {mem.available // (1024 ** 2)} MB
Usada: {mem.used // (1024 ** 2)} MB
Porcentaje en uso: {mem.percent}%
"""

# Obtener Informacion de la memoria fisica
def get_disk_info():
    result = ""
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            result += f"""
Unidad: {part.device}
  Sistema de archivos: {part.fstype}
  Total: {usage.total // (1024 ** 3)} GB
  Usado: {usage.used // (1024 ** 3)} GB ({usage.percent}%)
"""
        except PermissionError:
            continue
    return result.strip()

# Obtener informacion de la red donde esta el windows
def get_network_info():
    result = ""
    for iface, addrs in psutil.net_if_addrs().items():
        result += f"\nInterfaz: {iface}\n"
        for addr in addrs:
            result += f"  {addr.family.name if hasattr(addr.family, 'name') else addr.family}: {addr.address}\n"
    return result.strip()

# Obtener los procesos del computador windows
def get_processes():
    output = ""
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent']):
        try:
            output += f"{proc.info['pid']:>5}  {proc.info['name'][:25]:<25}  {proc.info['username']:<20}  {proc.info['cpu_percent']}%\n"
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return output

def get_installed_programs():
    return run_command('wmic product get name,version')

def get_users():
    return run_command("net user")

def get_services():
    return run_command("sc query")

def get_bios_info():
    try:
        c = wmi.WMI()
        bios = c.Win32_BIOS()[0]
        return f"Fabricante: {bios.Manufacturer}\nVersión: {bios.SMBIOSBIOSVersion}\nFecha: {bios.ReleaseDate}"
    except Exception as e:
        return f"Error accediendo a la BIOS: {e}"

def get_env_variables():
    return "\n".join(f"{k}={v}" for k, v in os.environ.items())

def get_updates():
    return run_command("powershell Get-HotFix")

# En el main se ejecutan los comandos y se guardan en un txt el resultados
def main():
    save_output("01_sistema.txt", get_system_info())
    save_output("02_cpu.txt", get_cpu_info())
    save_output("03_memoria.txt", get_memory_info())
    save_output("04_disco.txt", get_disk_info())
    save_output("05_red.txt", get_network_info())
    save_output("06_procesos.txt", get_processes())
    save_output("07_programas.txt", get_installed_programs())
    save_output("08_usuarios.txt", get_users())
    save_output("09_servicios.txt", get_services())
    save_output("10_bios.txt", get_bios_info())
    save_output("11_entorno.txt", get_env_variables())
    save_output("12_actualizaciones.txt", get_updates())

    print(f"\n (+) Información guardada en la carpeta: {output_dir}")

if __name__ == "__main__":
    main()
