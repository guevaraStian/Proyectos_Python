# Este es un codigo para extraer la mayor cantidad de informacion de
# Un sistema operativo Linux, como requisito hay que descargar
# El software y luego instalar las librerias de python
# Por ultimo dar los permisos adminin al archivo o terminal
# # pip install psutil distro


import os
import platform
import socket
import subprocess
import psutil
import distro
from datetime import datetime

# Crear carpeta con nombre basado en hostname y fecha
OUTPUT_DIR = f"Info_Linux_{socket.gethostname()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_output(name, command):
    path = os.path.join(OUTPUT_DIR, f"{name}.txt")
    try:
        with open(path, "w", encoding="utf-8") as f:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=True, text=True)
            f.write(result.stdout.strip())
        print(f"[+] Guardado: {name}")
    except Exception as e:
        print(f"[-] Error guardando {name}: {e}")

def save_text(name, content):
    with open(os.path.join(OUTPUT_DIR, f"{name}.txt"), "w", encoding="utf-8") as f:
        f.write(content)

# Información del sistema
save_text("sistema", f"""\
Hostname: {socket.gethostname()}
Usuario: {os.getlogin()}
Distro: {distro.name()} {distro.version()} ({distro.codename()})
Kernel: {platform.release()}
Arquitectura: {platform.machine()}
Procesador: {platform.processor()}
Python: {platform.python_version()}
""")

# Variables de entorno
save_text("entorno", "\n".join(f"{k}={v}" for k, v in os.environ.items()))

# CPU y memoria
save_text("cpu_memoria", f"""\
CPUs: {psutil.cpu_count(logical=True)} (físicos: {psutil.cpu_count(logical=False)})
Uso CPU: {psutil.cpu_percent(interval=1)}%
RAM total: {psutil.virtual_memory().total // (1024**2)} MB
RAM usada: {psutil.virtual_memory().used // (1024**2)} MB
""")

# Disco
save_output("discos", "lsblk -o NAME,FSTYPE,SIZE,MOUNTPOINT,UUID")
save_output("espacio_disco", "df -hT")
save_output("parted", "sudo parted -l")

# Hardware
save_output("cpu_info", "lscpu")
save_output("bios", "sudo dmidecode -t bios")
save_output("motherboard", "sudo dmidecode -t baseboard")
save_output("memoria", "sudo dmidecode -t memory")

# Red
save_output("ip_addr", "ip a")
save_output("ip_route", "ip r")
save_output("interfaces", "cat /etc/network/interfaces")
save_output("resolv_conf", "cat /etc/resolv.conf")
save_output("netstat", "netstat -tulnpe")
save_output("ss", "ss -tulnp")

# Usuarios y grupos
save_output("usuarios", "cut -d: -f1 /etc/passwd")
save_output("grupos", "cut -d: -f1 /etc/group")
save_output("sudoers", "cat /etc/sudoers")
save_output("logged_users", "w")

# Servicios y procesos
save_output("procesos", "ps aux --sort=-%mem | head -n 20")
save_output("servicios_activos", "systemctl list-units --type=service --state=running")
save_output("todos_servicios", "systemctl list-unit-files --type=service")

# Paquetes instalados
if os.path.exists("/usr/bin/dpkg"):
    save_output("paquetes", "dpkg -l")
elif os.path.exists("/usr/bin/rpm"):
    save_output("paquetes", "rpm -qa")
elif os.path.exists("/usr/bin/pacman"):
    save_output("paquetes", "pacman -Q")

# Dispositivos conectados
save_output("lspci", "lspci")
save_output("lsusb", "lsusb")

# Firewall
save_output("iptables", "sudo iptables -L -v -n")
save_output("nftables", "sudo nft list ruleset")

# Logs del sistema
save_output("syslog", "tail -n 100 /var/log/syslog")
save_output("auth_log", "tail -n 100 /var/log/auth.log")
save_output("dmesg", "dmesg | tail -n 100")

print(f"\n (+) Información recopilada en: {OUTPUT_DIR}/")