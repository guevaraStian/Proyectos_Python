# En este codigo se muestra un decodificador FM de señales de radio
# y tambien como usar la libreria RtlSdr
# pip install numpy scipy matplotlib sounddevice pyrtlsdr
import numpy as np
from rtlsdr import RtlSdr
import matplotlib.pyplot as plt
from scipy.signal import decimate, butter, lfilter
import sounddevice as sd


# Inicializar el SDR
Radio_frecuencia = RtlSdr()
Radio_frecuencia.sample_rate = 2.4e6       # Hz
Radio_frecuencia.center_freq = 100.0e6     # 100 MHz, cambia a una estación local
Radio_frecuencia.gain = 40

def fm_demodulate(iq_signal):
    angle = np.angle(iq_signal[1:] * np.conj(iq_signal[:-1]))
    return angle

# Filtro pasa-bajo para aislar canal de audio
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    norm_cutoff = cutoff / nyq
    b, a = butter(order, norm_cutoff, btype='low')
    return b, a

def lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    return lfilter(b, a, data)

# Creamos un bucle para recibir la señal
try:
    print("Se muestra la señal que esta modulada en FM")
    while True:
        Muestra_ejemplo = Radio_frecuencia.read_samples(256*1024)

        # Demodular FM
        demodulated = fm_demodulate(Muestra_ejemplo)

        # Filtrar y decimar para obtener audio (de ~2400000 Hz a 48000 Hz)
        audio = lowpass_filter(demodulated, cutoff=16e3, fs=2.4e6)
        audio = decimate(audio, int(2.4e6 / 48e3))

        # Procedemos a normalizar el audio con np
        audio /= np.max(np.abs(audio))
        
        # Reproducir audio
        sd.play(audio, 48000, blocking=True)

except KeyboardInterrupt:
    print("\n En espera...")
finally:
    Radio_frecuencia.close()
    sd.stop()