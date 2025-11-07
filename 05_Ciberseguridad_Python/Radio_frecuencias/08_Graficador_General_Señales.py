# En este ejemplo de codigo se muestra la creacion de un radar
# con la distancia de los dispositivos drones cerca
# pip install pyrtlsdr numpy matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parámetros de la señal
fs = 10000          # Frecuencia de muestreo (Hz)
duration = 0.01     # Duración de cada frecuencia (segundos)
f_start = 1       # Frecuencia inicial (Hz)
f_end = 3e12        # Frecuencia final (Hz)
step_freq = 100     # Paso de frecuencia (Hz)

# Tiempo para cada segmento
t = np.arange(0, duration, 1/fs)

# Arreglo para almacenar toda la señal
signal = np.array([])
frequencies = []

# Generar la señal para cada frecuencia
for f in range(f_start, f_end + 1, step_freq):
    segment = np.sin(2 * np.pi * f * t)
    signal = np.concatenate((signal, segment))
    frequencies.extend([f]*len(segment))

# Crear vector de tiempo global
total_time = np.arange(0, len(signal)) / fs

# Graficar señal
plt.figure(figsize=(10, 4))
plt.plot(total_time, signal)
plt.title("Señal con barrido de frecuencia")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.tight_layout()
plt.show()

# Guardar muestras en archivo CSV
df = pd.DataFrame({
    'Tiempo (s)': total_time,
    'Amplitud': signal,
    'Frecuencia (Hz)': frequencies
})
df.to_csv("senal_barrido_frecuencia.csv", index=False)
print("Archivo CSV guardado como 'senal_barrido_frecuencia.csv'")








