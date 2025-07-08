# En este codigo se muestra un analisador de señales de radio
# y tambien como usar la libreria RtlSdr
# pip install numpy matplotlib pyrtlsdr scipy

import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr
import time

# Primero inicializamos el RtlSdr
Radio_frecuencia = RtlSdr()

# Luego procedemos a configurar sus caracteristicas
Radio_frecuencia.sample_rate = 2.4e6   # Frecuencia de muestreo (Hz)
Radio_frecuencia.center_freq = 100e6   # Frecuencia central (Hz) — puedes cambiarla, por ejemplo 100 MHz
Radio_frecuencia.gain = 'auto'         # Ganancia automática

# Tambien usamos matplot para crear la grafica que muestra la señal
plt.ion()
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=1)
ax.set_xlim(0, Radio_frecuencia.sample_rate / 1e6)
ax.set_ylim(-100, 0)
ax.set_xlabel('Frecuencia (MHz)')
ax.set_ylabel('Potencia (dB)')

# Esta funcion muestra como sacar datos de la señal escogida
def update_spectrum():
    Muestra_ejemplo = Radio_frecuencia.read_samples(256*1024)
    # Calcular FFT y convertir a escala logarítmica
    fft_vals = np.fft.fftshift(np.fft.fft(Muestra_ejemplo))
    psd = 20 * np.log10(np.abs(fft_vals))
    freqs = np.linspace(-Radio_frecuencia.sample_rate/2, Radio_frecuencia.sample_rate/2, len(psd)) / 1e6  # MHz

    # Se ingresan los datos a la grafica
    line.set_xdata(freqs)
    line.set_ydata(psd)
    fig.canvas.draw()
    fig.canvas.flush_events()

# Se crea un while para mostrar la grafica en tiempo real
print("Se esta mostrando en pantalla la señal de radio")
try:
    while True:
        update_spectrum()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\n Se detuvo por orden del usuario.")
finally:
    Radio_frecuencia.close()