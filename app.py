from flask import Flask, render_template, request
import os
import random

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

        mood_name = result["mood"]

        recommendations = {

            "Happy 😊": [
                "Levitating - Dua Lipa",
                "Espresso - Sabrina Carpenter",
                "Blinding Lights - The Weeknd",
                "Happy - Pharrell Williams",
                "Good Time - Owl City",
                "Firework - Katy Perry",
                "Sugar - Maroon 5",
                "Can't Stop The Feeling - Justin Timberlake",
                "Shut Up and Dance - WALK THE MOON",
                "Cake By The Ocean - DNCE"
            ],

            "Sad 😔": [
               "Someone Like You - Adele",
               "Fix You - Coldplay",
               "Let Her Go - Passenger",
               "Photograph - Ed Sheeran",
               "When We Were Young - Adele",
               "Say Something - A Great Big World",
               "Before You Go - Lewis Capaldi",
               "All I Want - Kodaline",
               "Arcade - Duncan Laurence",
               "Happier - Olivia Rodrigo"
            ],

            "Energetic ⚡": [
               "Believer - Imagine Dragons",
               "Thunder - Imagine Dragons",
               "Can't Hold Us - Macklemore",
               "Stronger - Kanye West",
               "Titanium - David Guetta",
               "Hall of Fame - The Script",
               "Remember The Name - Fort Minor",
               "Eye of the Tiger - Survivor",
               "Power - Kanye West",
               "Animals - Martin Garrix"
           ],

             "Chill 🌙": [
              "Sunflower - Post Malone",
              "Perfect - Ed Sheeran",
              "Yellow - Coldplay",
              "Lovely - Billie Eilish",
              "Ocean Eyes - Billie Eilish",
              "Heather - Conan Gray",
              "Night Changes - One Direction",
              "Until I Found You - Stephen Sanchez",
              "Dandelions - Ruth B",
              "Stay - Rihanna"
            ]
        }

        songs = random.sample(
            recommendations.get(mood_name, []),
             min(3, len(recommendations.get(mood_name, [])))
        )

        if "Happy" in mood_name:
            explanation = "This song was classified as Happy because it has a relatively high tempo and energetic audio characteristics."

        elif "Sad" in mood_name:
            explanation = "This song was classified as Sad because it has lower energy and a calmer musical pattern."

        elif "Energetic" in mood_name:
            explanation = "This song was classified as Energetic because it has a very high tempo and strong energy level."

        else:
            explanation = "This song was classified as Chill because it has a balanced tempo and relaxed energy profile."

        return render_template(
         "result.html",
         mood=result["mood"],
         tempo=result["tempo"],
         energy=result["energy"],
         confidence=result["confidence"],
         songs=songs,
         explanation=explanation,
         mfcc=result["mfcc"],
         spectral_centroid=result["spectral_centroid"],
         zero_crossing_rate=result["zero_crossing_rate"]
)
    return "Upload Failed"


if __name__ == "__main__":
    app.run(debug=True)