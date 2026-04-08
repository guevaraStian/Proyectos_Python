# Pasar de audio a texto
# Usando whisper y Sklearn
# Archivo TXT 
# pip install numpy scipy librosa soundfile torch torchaudio pyannote.audio openai-whisper tqdm
import whisper
import librosa
import soundfile as sf
import numpy as np
from tqdm import tqdm
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler

# Creacion de variables necesarias
audio_file = "mi_audio.wav"
output_txt = "transcripcion_3.txt"
model_size = "large"  # modelo más preciso de Whisper
min_silence_len = 0.5  # segundos de silencio para separar turnos
silence_thresh = 0.01  # nivel de RMS considerado silencio
sr_target = 16000       # frecuencia de muestreo deseada

# Se carga en el software el audio indicado
y, sr = librosa.load(audio_file, sr=sr_target)
duration = librosa.get_duration(y=y, sr=sr)
print(f"Duración del audio: {duration:.2f} segundos")

# Se detectan silencios y momentos de habla
rms = librosa.feature.rms(y=y)[0]
frames = np.arange(len(rms))
times = librosa.frames_to_time(frames, sr=sr, hop_length=512)

segments = []
start_idx = 0
for i in range(1, len(rms)):
    if rms[i] < silence_thresh:
        if times[i] - times[start_idx] > min_silence_len:
            segments.append((times[start_idx], times[i]))
            start_idx = i+1
segments.append((times[start_idx], duration))
print(f"Se detectaron {len(segments)} segmentos de audio para transcripción.")

# Se extraen segmentos de frases para la transcripcion
segment_features = []

for start, end in segments:
    start_sample = int(start * sr)
    end_sample = int(end * sr)
    seg_audio = y[start_sample:end_sample]
    # Extraer MFCC como features de voz
    mfcc = librosa.feature.mfcc(y=seg_audio, sr=sr, n_mfcc=13)
    mfcc_mean = np.mean(mfcc, axis=1)
    segment_features.append(mfcc_mean)

# Normalizar features
scaler = StandardScaler()
X = scaler.fit_transform(segment_features)

# Se agrupan caracteristicas de voces particulares
n_voices = 2  # cambiar según cuántas voces esperes
clustering = AgglomerativeClustering(n_clusters=n_voices)
labels = clustering.fit_predict(X)

# Se carga el modelo whisper
print("Cargando modelo Whisper...")
model = whisper.load_model(model_size)
print("Modelo cargado con éxito.\n")

# Se transcriben los segementos de frases de voz
transcriptions = []

for i, (start, end) in enumerate(tqdm(segments, desc="Transcribiendo segmentos", unit="segment")):
    start_sample = int(start * sr)
    end_sample = int(end * sr)
    segment_audio = y[start_sample:end_sample]
    
    temp_file = "temp_segment.wav"
    sf.write(temp_file, segment_audio, sr)
    
    result = model.transcribe(temp_file, language="es", fp16=False, verbose=False)
    text = result["text"].strip()
    
    if text:
        voz_id = f"Voz {labels[i]+1}"  # +1 para mostrar Voz 1, Voz 2...
        transcriptions.append((voz_id, text))

# Se guarda la transcripcion en un .txt
with open(output_txt, "w", encoding="utf-8") as f:
    for speaker, text in transcriptions:
        f.write(f"{speaker}: {text}\n")

print(f"\nTranscripción completa guardada en '{output_txt}'")