import numpy as np
import sounddevice as sd

# Parámetros del sonido
frecuencia = 25000  # Frecuencia en Hz (ultrasonido)
duracion = 5      # Duración de un ciclo base
fs = 48000          # Frecuencia de muestreo

# Crear onda base
t = np.linspace(0, duracion, int(fs * duracion), endpoint=False)
onda = np.sin(2 * np.pi * frecuencia * t)

# Normalizar para 16 bits
onda = np.int16(onda * 32767)

print("Reproduciendo ultrasonido en bucle. Presiona Ctrl+C para detener...")

try:
    while True:
        sd.play(onda, fs)
        sd.wait()  # Espera a que termine antes de repetir
except KeyboardInterrupt:
    print("\nReproducción detenida.")
