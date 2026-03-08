# Pasar de audio a texto
# Usando whisper y pydub
# Archivo TXT 
# pip install openai-whisper pydub soundfile numpy
import whisper  
import soundfile as sf
import numpy as np
import os
import librosa
from scipy.spatial.distance import cosine

# --- Configuración ---
audio_file = "mi_audio.wav"  # Solo wav
output_txt = "transcripcion_por_voces.txt"

# --- Cargar audio ---
y, sr = sf.read(audio_file)
print(f"Audio cargado: {len(y)/sr:.2f} segundos")

# --- Detectar segmentos de voz simple por energía ---
frame_len = int(sr * 0.5)  # ventanas de 0.5 s
energy = [np.sum(np.abs(y[i:i+frame_len])) for i in range(0, len(y), frame_len)]
threshold = np.percentile(energy, 50)  # umbral de energía
segments = []
start = None

for i, e in enumerate(energy):
    t = i * 0.5  # tiempo en segundos
    if e > threshold and start is None:
        start = t
    elif e <= threshold and start is not None:
        end = t
        segments.append((start, end))
        start = None
if start is not None:
    segments.append((start, len(y)/sr))

print(f"{len(segments)} segmentos detectados")

# --- Cargar modelo Whisper ---
model = whisper.load_model("base")

# --- Función para obtener MFCC promedio de un segmento ---
def mfcc_embedding(y_segment, sr, n_mfcc=13):
    mfccs = librosa.feature.mfcc(y=y_segment, sr=sr, n_mfcc=n_mfcc)
    return np.mean(mfccs, axis=1)

# --- Diccionario para voces ya identificadas ---
voice_embeddings = []
voice_names = []

# --- Transcribir segmentos en español y asignar voz ---
with open(output_txt, "w", encoding="utf-8") as f:
    for i, (start, end) in enumerate(segments):
        start_sample = int(start * sr)
        end_sample = int(end * sr)
        segment_audio = y[start_sample:end_sample]

        # Guardar temporal
        tmp_file = f"segmento_temp_{i}.wav"
        sf.write(tmp_file, segment_audio, sr)

        # Transcribir en español
        result = model.transcribe(tmp_file, task="transcribe", language="es")
        text = result["text"].strip()

        if text:
            # Calcular MFCC del segmento
            embedding = mfcc_embedding(segment_audio, sr)

            # Comparar con voces anteriores
            assigned_voice = None
            for idx, prev_emb in enumerate(voice_embeddings):
                if cosine(embedding, prev_emb) < 0.4:  # umbral de similitud
                    assigned_voice = voice_names[idx]
                    break

            if assigned_voice is None:
                # Nueva voz
                assigned_voice = f"Voz {len(voice_embeddings)+1}"
                voice_embeddings.append(embedding)
                voice_names.append(assigned_voice)

            f.write(f"{assigned_voice}: {text}\n")

        os.remove(tmp_file)

print(f"Transcripción en español guardada en {output_txt}")