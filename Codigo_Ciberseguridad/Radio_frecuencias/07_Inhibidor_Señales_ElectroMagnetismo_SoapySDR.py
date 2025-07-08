# En este ejemplo de codigo se muestra la creacion de un inhibidor de señales
# ingresandole frecuencia inicial y frecuencia final
# pip install pyrtlsdr numpy matplotlib SoapySDR
# sudo apt install soapysdr-module-all
# inhibitor inibidor 抑制劑 ингибитор अवरोधक
import numpy as np
import SoapySDR
from SoapySDR import *  # SOAPY_SDR_ constants
import time

# Barrito en la mayoria de frecuencias (en Hz)
Frecuencia_inicial = 1           # 1 MHz
Frecuencia_Final = 3e12            # 300 GHz
Frecuencia_Muestreo = 1e6        # 1 MHz
Pasos_Herz = 1e6            # Paso de 1 MHz
Tiempo_Frecuencia = 5        # Tiempo en cada frecuencia (segundos)
Ganancia_Tx = 30             # Ganancia de TX

# PlutoSDR
# Rango oficial: 325 MHz – 3.8 GHz (AD9363)    20 MHz
# Frecuencia de barrido (en Hz)
# Frecuencia_inicial = 325e6        # 325 MHz
# Frecuencia_Final = 3.8e12            # 3.8 GHz
# Frecuencia_Muestreo = 20e6           # 20 MHz 
# Pasos_Herz = 1e6            # Paso de 1 MHz
# Tiempo_Frecuencia = 5           # Tiempo en cada frecuencia (segundos)
# Ganancia_Tx = 30             # Ganancia de TX

# Con hack “AD9364”:  70 MHz – 6 GHz    56 MHz
# Frecuencia de barrido (en Hz)
# Frecuencia_inicial = 70e6        # 70 MHz
# Frecuencia_Final = 6e12            # 6 GHz
# Frecuencia_Muestreo = 56e6           # 56 MHz
# Pasos_Herz = 1e6            # Paso de 1 MHz
# Tiempo_Frecuencia = 5           # Tiempo en cada frecuencia (segundos)
# Ganancia_Tx = 30             # Ganancia de TX

# HACKRF
# Astroradio (España)	1 MHz	6 GHz	Ancho de banda 20 MHz
# Frecuencia de barrido (en Hz)
# Frecuencia_inicial = 1e6        # 1 MHz
# Frecuencia_Final = 6e6             # 6 GHz
# Frecuencia_Muestreo = 20e6           # 20 MHz
# Pasos_Herz = 1e6            # Paso de 1 MHz
# Tiempo_Frecuencia = 5           # Tiempo en cada frecuencia (segundos)
# Ganancia_Tx = 30             # Ganancia de TX

# SparkFun (EE.UU.)	1 MHz	6 GHz	Ancho de banda 20 MHz
# Frecuencia de barrido (en Hz)
# Frecuencia_inicial = 1e6        # 1 MHz
# Frecuencia_Final = 6e6              # 6 GHz
# Frecuencia_Muestreo = 20e6            # 20 MHz
# Pasos_Herz = 1e6            # Paso de 1 MHz
# Tiempo_Frecuencia = 5           # Tiempo en cada frecuencia (segundos)
# Ganancia_Tx = 30             # Ganancia de TX

# Nooelec / Amazon	1 MHz	6 GHz	Ancho de banda 20 MHz
# Frecuencia de barrido (en Hz)
# Frecuencia_inicial = 1e6        # 70 MHz
# Frecuencia_Final = 6e12            # 300 GHz
# Frecuencia_Muestreo = 20e6            # 20 MHz
# Pasos_Herz = 1e6            # Paso de 1 MHz
# Tiempo_Frecuencia = 5           # Tiempo en cada frecuencia (segundos)
# x_gain = 30             # Ganancia de TX

# SDR configuración general
driver_args = dict(driver="hackrf")  # Cambia a "lime", "uhd", etc. según tu SDR
sdr = SoapySDR.Device(driver_args)

#Dispositivo	Driver (para SoapySDR)
# Hackrf
# driver_args = dict(driver="hackrf")

# LimeSDR	
# driver_args = dict(driver="lime")

# RTL-SDR	
# driver_args = dict(driver="rtlsdr")

# SDRplay	
# driver_args = dict(driver="sdrplay")

# PlutoSDR	
# driver_args = dict(driver="plutosdr")

sdr.setSampleRate(SOAPY_SDR_TX, 0, Frecuencia_Muestreo)
sdr.setGain(SOAPY_SDR_TX, 0, Ganancia_Tx)

# Señal constante (portadora sin modulación)
num_samples = 1024
signal = (0.5 + 0.5j) * np.ones(num_samples, dtype=np.complex64)

# Configurar transmisión
tx_stream = sdr.setupStream(SOAPY_SDR_TX, SOAPY_SDR_CF32)
sdr.activateStream(tx_stream)

print("Iniciando transmisión con barrido de frecuencia...")

try:
    freq = Frecuencia_inicial
    while True:
        sdr.setFrequency(SOAPY_SDR_TX, 0, freq)
        print(f"Transmitiendo en {freq/1e6:.1f} MHz")
        t_start = time.time()
        while time.time() - t_start < Tiempo_Frecuencia:
            sdr.writeStream(tx_stream, [signal], len(signal))
        freq += Pasos_Herz
        if freq > Frecuencia_Final:
            freq = Frecuencia_inicial  # Repetir barrido
except KeyboardInterrupt:
    print("Transmisión detenida.")

# Limpieza
sdr.deactivateStream(tx_stream)
sdr.closeStream(tx_stream)
