# En este ejemplo de codigo se muestra la creacion de un radar
# con la distancia de los celulares que estan cerca
# sudo apt update
# sudo apt install rtl-sdr
# pip install pyrtlsdr numpy matplotlib

import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr
import time

# Configurar el SDR
sdr = RtlSdr()
sdr.sample_rate = 1e6       # 1 MHz
sdr.center_freq = 945e6     # frecuencia objetivo (ajustable)
sdr.gain = 'auto'

# Claro 2G/3G: 1900 MHz (B2), 850 MHz (B5)
# sdr.center_freq = 1900e6

# Movistar 2G/3G: 1900 MHz (B2), 850 MHz (B5)
# sdr.center_freq = 850e6

# Tigo LTE: AWS 1700/2100 (B4), 700 MHz (B28), 2600 MHz (B7)
# sdr.center_freq = 1700e6

# Avantel / ETB  3G: 850 MHz (B5) o 1900 MHz (B2)
# sdr.center_freq = 850e6

# WOM LTE: 700 MHz (B28), 2600 MHz (B7)
# sdr.center_freq = 700e6

# sdr.center_freq = [1900ee6, 850e6, 1700e6, 700e6]

# Función para medir la potencia de señal
def measure_power():
    samples = sdr.read_samples(256*1024)
    power = 10 * np.log10(np.mean(np.abs(samples)**2))
    return power

# Escaneo simple
try:
    powers = []
    times = []

    print("Escaneando actividad GSM... Ctrl+C para detener.")
    start_time = time.time()

    while True:
        p = measure_power()
        t = time.time() - start_time
        powers.append(p)
        times.append(t)
        print(f"[{round(t,1)}s] Potencia: {round(p,2)} dB")

        time.sleep(0.5)  # Ajusta el intervalo

except KeyboardInterrupt:
    print("\nFinalizado.")

finally:
    sdr.close()

# Graficar resultados
plt.plot(times, powers)
plt.xlabel("Tiempo (s)")
plt.ylabel("Potencia (dB)")
plt.title("Actividad GSM Detectada")
plt.grid(True)
plt.show()

