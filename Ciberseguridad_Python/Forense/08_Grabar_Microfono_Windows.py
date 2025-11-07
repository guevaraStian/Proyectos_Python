# Este es un codigo para grabar microfono de un computador
# Un sistema operativo microsoft
# El software y luego instalar las librerias de python
# Por ultimo dar los permisos adminin al archivo o terminal
# pip install sounddevice scipy requests

import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import time
from datetime import datetime
import requests

# Parámetros
duracion_segundos = 5       # Duración de la grabación
frecuencia_muestreo = 44100 # Frecuencia de muestreo estándar en Hz (CD Quality)

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




print("(+) Grabando...")
audio = sd.rec(int(duracion_segundos * frecuencia_muestreo), samplerate=frecuencia_muestreo, channels=2)
sd.wait()  # Espera a que termine la grabación
print("(+) Grabación terminada.")

# Guardar como archivo WAV
archivo_salida = "Grabacion_{Tiempo_Inicial}_{Ubicacion}.wav"
write(archivo_salida, frecuencia_muestreo, audio)
print(f"(+) Audio guardado como: {archivo_salida}")





# Cargar archivo .wav
nombre_archivo = 'Grabacion_{Tiempo_Inicial}_{Ubicacion}.wav'  # Cambia esto por tu archivo
frecuencia_muestreo, datos = wavfile.read(nombre_archivo)

# Si el archivo es estéreo, convertir a mono
if len(datos.shape) == 2:
    datos = datos.mean(axis=1)

# Normalizar el audio (si está en int16)
datos = datos / np.max(np.abs(datos))

# Calcular energía en ventana (RMS)
ventana_tamaño = 1024  # muestras por bloque
rms = np.sqrt(np.convolve(datos**2, np.ones(ventana_tamaño)/ventana_tamaño, mode='valid'))

# Convertir a decibeles (referencia 1.0)
decibeles = 20 * np.log10(rms + 1e-10)  # se agrega 1e-10 para evitar log(0)

# Crear eje de tiempo
tiempo = np.linspace(0, len(decibeles)/frecuencia_muestreo, num=len(decibeles))

# Graficar
plt.figure(figsize=(10, 4))
plt.plot(tiempo, decibeles)
plt.title('Nivel de sonido en dB (estimado)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Nivel [dB]')
plt.grid()
plt.tight_layout()
plt.show()







