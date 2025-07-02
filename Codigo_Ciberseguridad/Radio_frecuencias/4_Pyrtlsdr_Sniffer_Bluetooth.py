# En este codigo se muestra un ejemplo de escaner de bluetooth
# y tambien como usar la libreria RtlSdr
# pip install numpy scipy matplotlib sounddevice pyrtlsdr
from rtlsdr import RtlSdr
import numpy as np
import matplotlib.pyplot as plt

# Configuración del SDR (ejemplo en canal 37 de BLE)
Radio_frecuencia = RtlSdr()
Radio_frecuencia.sample_rate = 2.4e6
Radio_frecuencia.center_freq = 2.402e9  # Canal 37
Radio_frecuencia.gain = 40

# Captura muestras
Muestra_ejemplo = Radio_frecuencia.read_samples(256*1024)
Radio_frecuencia.close()

# Visualiza espectro
fft = np.fft.fftshift(np.fft.fft(Muestra_ejemplo))
psd = 20 * np.log10(np.abs(fft))
freqs = np.linspace(-Radio_frecuencia.sample_rate/2, Radio_frecuencia.sample_rate/2, len(psd)) / 1e6

plt.plot(freqs, psd)
plt.title("BLE Spectrogram (Canal 37)")
plt.xlabel("Frecuencia (MHz)")
plt.ylabel("Potencia (dB)")
plt.grid(True)
plt.show()