import librosa
import numpy as np

def analyze_audio(file_path):

    y, sr = librosa.load(file_path)

    tempo = librosa.beat.tempo(y=y, sr=sr)

    energy = np.mean(librosa.feature.rms(y=y))

    tempo_value = float(tempo[0])

    if tempo_value > 140 and energy > 0.15:
        mood = "Energetic ⚡"

    elif tempo_value > 110:
        mood = "Happy 😊"

    elif energy < 0.05:
        mood = "Sad 😔"

    else:
        mood = "Chill 🌙"

    return {
        "mood": mood,
        "tempo": round(tempo_value, 2),
        "energy": round(float(energy), 4)
    }