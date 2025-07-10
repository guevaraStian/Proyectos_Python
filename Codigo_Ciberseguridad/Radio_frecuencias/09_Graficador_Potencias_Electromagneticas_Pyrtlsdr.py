# En este ejemplo de codigo se muestra un graficador de potencias electromagneticas
# con la distancia de los dispositivos en una frecuencia
# pip install pyrtlsdr matplotlib numpy
import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr

# Parámetros del barrido
freq_start = 88e6     # Frecuencia inicial en Hz (por ejemplo, 88 MHz)
freq_end = 108e6      # Frecuencia final en Hz (por ejemplo, 108 MHz)
freq_step = 2e6       # Paso de frecuencia (ancho de banda de la muestra), típico ~2 MHz
sample_rate = 2.4e6   # Tasa de muestreo en Hz
num_samples = 1024    # Número de muestras por paso

# Inicializa el SDR
sdr = RtlSdr()
sdr.sample_rate = sample_rate
sdr.gain = 'auto'

frequencies = []
powers = []

try:
    freqs = np.arange(freq_start, freq_end, freq_step)

    for freq in freqs:
        print(f"Escaneando {freq / 1e6:.2f} MHz...")
        sdr.center_freq = freq
        samples = sdr.read_samples(num_samples)
        
        # FFT y cálculo de potencia
        power = np.abs(np.fft.fftshift(np.fft.fft(samples)))**2
        power_db = 10 * np.log10(power)
        freqs_axis = np.linspace(freq - sample_rate/2, freq + sample_rate/2, num_samples)
        
        frequencies.extend(freqs_axis)
        powers.extend(power_db)

finally:
    sdr.close()

# Graficar
plt.figure(figsize=(12, 6))
plt.plot(np.array(frequencies)/1e6, powers, lw=0.5)
plt.title("Espectro de Frecuencia (Barrido RTL-SDR)")
plt.xlabel("Frecuencia (MHz)")
plt.ylabel("Potencia (dB)")
plt.grid(True)
plt.tight_layout()
plt.show()







