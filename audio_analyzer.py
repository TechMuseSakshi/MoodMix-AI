import librosa
import numpy as np
import joblib

# Load trained model
model = joblib.load("models/mood_model.pkl")

def analyze_audio(file_path):

    y, sr = librosa.load(file_path)

    tempo = librosa.beat.tempo(y=y, sr=sr)
    energy = np.mean(librosa.feature.rms(y=y))

    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr))

    spectral_centroid = np.mean(
     librosa.feature.spectral_centroid(y=y, sr=sr)
    )

    zero_crossing_rate = np.mean(
        librosa.feature.zero_crossing_rate(y)
    )

    tempo_value = float(tempo[0])
    energy_value = float(energy)

    # Predict mood using ML model
    mood = model.predict([[tempo_value, energy_value]])[0]

    confidence = max(model.predict_proba([[tempo_value, energy_value]])[0]) * 100

    # Add emoji
    mood_emojis = {
        "Happy": "Happy 😊",
        "Sad": "Sad 😔",
        "Energetic": "Energetic ⚡",
        "Chill": "Chill 🌙"
    }

    mood = mood_emojis.get(mood, mood)

    return{
    "mood": mood,
    "tempo": round(tempo_value, 2),
    "energy": round(float(energy), 4),
    "confidence": round(confidence, 2),
    "mfcc": round(float(mfcc), 2),
    "spectral_centroid": round(float(spectral_centroid), 2),
    "zero_crossing_rate": round(float(zero_crossing_rate), 4)
}