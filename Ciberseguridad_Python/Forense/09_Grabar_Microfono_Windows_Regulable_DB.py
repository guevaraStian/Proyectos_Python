# Este es un codigo grabar el microfono de la victima regulando los decibeles
# Un sistema operativo Android, como requisito hay que descargar
# El software y luego instalar las librerias de python
# Por ultimo dar los permisos adminin al archivo o terminal
# pip install sounddevice scipy numpy matplotlib requests

import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import queue
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import time
from datetime import datetime
import requests

# Configuración
samplerate = 44100
channels = 1
block_duration = 0.1  # segundos por bloque
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

def db_level(audio_block):
    """Calcula decibel RMS del bloque"""
    rms = np.sqrt(np.mean(np.square(audio_block)))
    return 20 * np.log10(rms) if rms > 0 else -np.inf

def get_user_inputs():
    while True:
        try:
            min_db = float(input("(+) Ingrese decibel mínimo (1–120): "))
            max_db = float(input("(+) Ingrese decibel máximo (1–120): "))
            duration = float(input("(+) Ingrese duración de grabación (segundos): "))
            if not (1 <= min_db <= max_db <= 120) or duration <= 0:
                print("(-) Revisa que los valores estén en el rango válido.")
                continue
            return min_db, max_db, duration
        except ValueError:
            print("(-) Entrada inválida. Usa números.")

def record_audio(min_db, max_db, duration):
    print(f"\n (+) Iniciando grabación por {duration} segundos...")

    total_frames = int(duration * samplerate)
    recorded_data = []

    start_time = time.time()
    current_second = 0

    def callback(indata, frames, time_info, status):
        nonlocal current_second
        if status:
            print(f"⚠️ {status}")
        recorded_data.append(indata.copy())
        elapsed = time.time() - start_time
        new_second = int(elapsed)
        if new_second > current_second:
            current_second = new_second
            level = db_level(indata)
            print(f"(+) Segundo: {current_second}/{int(duration)} - (+) Nivel: {level:.2f} dB")

    # Grabar audio
    with sd.InputStream(samplerate=samplerate, channels=channels, callback=callback):
        sd.sleep(int(duration * 1000))  # milisegundos

    # Guardar grabación
    audio_np = np.concatenate(recorded_data, axis=0)
    wav.write("Grabacion_{Tiempo_Inicial}_{Ubicacion}.wav", samplerate, audio_np)
    print("\n(+) Grabación finalizada. Archivo guardado como 'grabacion.wav'.")

if __name__ == "__main__":
    min_db, max_db, duration = get_user_inputs()
    record_audio(min_db, max_db, duration)

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
    plt.savefig("Grafica_{Tiempo_Inicial}_{Ubicacion}.png")  # Puedes usar .jpg, .svg, .pdf, etc.
    plt.close()  # Cierra la figura para liberar memoria







