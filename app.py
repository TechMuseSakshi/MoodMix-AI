from flask import Flask, render_template, request
import os

from models.audio_analyzer import analyze_audio

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/upload", methods=["POST"])
def upload():

    song = request.files["song"]

    if song:

        filepath = os.path.join("uploads", song.filename)

        song.save(filepath)

        result = analyze_audio(filepath)

        return render_template(
         "result.html",
          mood=result["mood"],
          tempo=result["tempo"],
          energy=result["energy"]
)

    return "Upload Failed"

if __name__ == "__main__":
    app.run(debug=True)