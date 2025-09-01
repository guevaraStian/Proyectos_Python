# Este es un codigo para extraer imagen de camara, imagen de pantalla y audio 
# Del entorno del computador windows
# El software y luego instalar las librerias de python
# pip install opencv-python mss numpy sounddevice scipy moviepy
import cv2
import numpy as np
import mss
import time
import sounddevice as sd
from scipy.io.wavfile import write as write_wav
from datetime import datetime
from moviepy.editor import VideoFileClip, AudioFileClip
import requests

respuesta = requests.get("https://ipinfo.io/json")
datos = respuesta.json()

print("(+) Ubicación aproximada:")
print(f"IP: {datos.get('ip')}")
print(f"Ciudad: {datos.get('city')}")
print(f"Región: {datos.get('region')}")
print(f"País: {datos.get('country')}")
print(f"Ubicación (lat,long): {datos.get('loc')}")
print(f"Organización: {datos.get('org')}")
print(f"Zona Horaria: {datos.get('timezone')}")
Ubicacion = datos.get('loc')



# Variables relacionados al proyecto
Duracion_Grabacion = 10  # segundos
Fps = 20
Tasa_Audio = 44100
Resolucion_Camara = (640, 480)
# Se calcula el tiempo inicial
Tiempo_Inicial = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')  # año-mes-día_hora-minuto-segundo

# Se guardan las variables de los nombres de archivos
archivo_camara = f"Camara_{Tiempo_Inicial}_{Ubicacion}.mp4"
archivo_pantalla = f"Pantalla_{Tiempo_Inicial}_{Ubicacion}.mp4"
archivo_audio = f"Audio_{Tiempo_Inicial}_{Ubicacion}.wav"
archivo_pantalla_con_audio = f"Pantalla_Audio_{Tiempo_Inicial}_{Ubicacion}.mp4"

# Se inicializa la camara
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, Resolucion_Camara[0])
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, Resolucion_Camara[1])

if not cam.isOpened():
    print("(-) No se pudo abrir la cámara")
    exit()

# Se organizan los datos de la camara
codec = cv2.VideoWriter_fourcc(*'mp4v')
out_camara = cv2.VideoWriter(archivo_camara, codec, Fps, Resolucion_Camara)

# Se graba el audio del windows
print("(+)(...) Guardando el audio...")
audio = sd.rec(int(Duracion_Grabacion * Tasa_Audio), samplerate=Tasa_Audio, channels=2)

# Se graba la pantalla mas la camara
with mss.mss() as sct:
    monitor = sct.monitors[1]  # pantalla completa principal
    screen_res = (monitor["width"], monitor["height"])
    out_pantalla = cv2.VideoWriter(archivo_pantalla, codec, Fps, screen_res)

    print("(+)(...) Guardando la imagen de camara y pantalla..")
    tiempo_inicio = time.time()

    while time.time() - tiempo_inicio < Duracion_Grabacion:
        # Se lee la camara
        ret, frame_cam = cam.read()
        if ret:
            out_camara.write(frame_cam)

        # Se lee la pantalla
        pantalla = np.array(sct.grab(monitor))
        frame_pantalla = cv2.cvtColor(pantalla, cv2.COLOR_BGRA2BGR)
        out_pantalla.write(frame_pantalla)

        time.sleep(1 / Fps)

# Guardar datos
sd.wait()
write_wav(archivo_audio, Tasa_Audio, audio)

# Inicializan librerias de guardar datos
cam.release()
out_camara.release()
out_pantalla.release()
cv2.destroyAllWindows()

# Se combina el audio con la imagen de la pantalla
print("(+)(...) Se esta combinando la imagen de la pantalla con el audio del microfono...")
video_clip = VideoFileClip(archivo_pantalla)
audio_clip = AudioFileClip(archivo_audio)
video_final = video_clip.set_audio(audio_clip)
video_final.write_videofile(archivo_pantalla_con_audio, codec='libx264', audio_codec='aac')

# Se muestra en pantalla los nombres de los archivos
print("\n(+) Grabación completada con éxito:")
print(f"(+) Archivo con imagen de Cámara:             {archivo_camara}")
print(f"(+) Archivo con imagen de pantalla:           {archivo_pantalla}")
print(f"(+) Archivo con pantalla + Audio:   {archivo_pantalla_con_audio}")



