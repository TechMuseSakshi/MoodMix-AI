import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
data = pd.read_csv("dataset/mood_dataset.csv")

# Features
X = data[["tempo", "energy"]]

# Target
y = data["mood"]

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "models/mood_model.pkl")

print("✅ Mood Model Trained Successfully!")