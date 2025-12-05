# Con este codigo se crea un software que emite sonido grabados
# En frecuencias no audibles
# Con la libreria de python Scapy
# pip install pydub simpleaudio numpy pydub ffmpeg-python

from pydub import AudioSegment
import numpy as np
import simpleaudio as sa
import os

# Se solicita el audio y la frecuencia a convertir
audio_path = input("Por favor ingrese el archivo MP3 o WAV: ")
freq = float(input("Por favor anexe la nueva frecuencia (Hz) para modificar el audio: "))

# Se carga el audio
audio = AudioSegment.from_file(audio_path)
samples = np.array(audio.get_array_of_samples()).astype(np.float32)
sample_rate = audio.frame_rate

print(f"La frecuencia original del audio es: {sample_rate} Hz")
print(f"La nueva frecuencia del audio es: {freq} Hz")

# La siguiente parte del codigo convierte el audio en los herz indicados
factor = freq / sample_rate  # escala del tiempo
indices = np.round(np.arange(0, len(samples), factor))
indices = indices[indices < len(samples)].astype(int)
modified_samples = samples[indices]

# Se quita la distorcion
modified_norm = modified_samples * (32767 / np.max(np.abs(modified_samples)))
modified_int16 = modified_norm.astype(np.int16)

# Se crea el audio MP3 con la nueva frecuencia
new_audio = AudioSegment(
    modified_int16.tobytes(),
    frame_rate=sample_rate,
    sample_width=2,
    channels=1
)

# Se guarda el archivo con el sonido
output_name = "audio_modificado.mp3"
new_audio.export(output_name, format="mp3")
print(f"El archivo generado es: {output_name}")

# Se procede a reproducir el audio
print("Reproduciendo el audio modificado…")
play_obj = sa.play_buffer(modified_int16, 1, 2, sample_rate)
play_obj.wait_done()

print("Fin del proceso")
