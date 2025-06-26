# En este codigo se muestra un ejemplo de receptor de señales de radio
# y tambien como usar la libreria RtlSdr
# pip install numpy scipy matplotlib sounddevice pyrtlsdr
import numpy as np
from rtlsdr import RtlSdr
from scipy.signal import decimate, butter, lfilter
import sounddevice as sd

# Se configuran las caracteristicas de sdr radio frecuencia
Radio_frecuencia = RtlSdr()
Radio_frecuencia.sample_rate = 2.4e6        # Frecuencia de muestreo
Radio_frecuencia.center_freq = 100.0e6      # Frecuencia de estación FM (100 MHz por ejemplo)
Radio_frecuencia.gain = 40

# Con la siguiente funcion se demodula la señal
def fm_demodulate(iq):
    phase = np.angle(iq[1:] * np.conj(iq[:-1]))
    return phase

# En la siguiente funcion se filtra la señal
def lowpass_filter(data, cutoff, fs, order=5):
    from scipy.signal import butter, lfilter
    nyq = 0.5 * fs
    norm_cutoff = cutoff / nyq
    b, a = butter(order, norm_cutoff, btype='low')
    return lfilter(b, a, data)

try:
    print("Se esta recibiendo la radio FM... Si quiere detenerlo CTL + C")
    while True:
        # Se capturan los datos actuales
        Muestra_ejemplo = Radio_frecuencia.read_samples(256*1024)

        # Demodulación FM
        audio = fm_demodulate(Muestra_ejemplo)

        # Filtro y reducción de tasa para reproducir como audio
        audio = lowpass_filter(audio, cutoff=16e3, fs=2.4e6)
        audio = decimate(audio, int(2.4e6 / 48e3))

        # Normalizar y reproducir
        audio /= np.max(np.abs(audio))
        sd.play(audio, 48000, blocking=True)

except KeyboardInterrupt:
    print("\n La Recepción de señal fue detenida.")
finally:
    Radio_frecuencia.close()
    sd.stop()


