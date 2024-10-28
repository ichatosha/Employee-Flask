from flask import Flask, render_template, request, redirect, url_for, flash
import pyttsx3
import qrcode
import os
from pydub import AudioSegment
from pydub.playback import play

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Replace with a strong secret key

# Directory for QR code images
QR_DIR = 'static/qr_codes'
os.makedirs(QR_DIR, exist_ok=True)

def play_audio(file_path):
    try:
        sound = AudioSegment.from_wav(file_path)
        play(sound)
    except Exception as e:
        print(f"Error playing audio: {e}")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        namefile = request.form["filename"]
        name = request.form["name"]
        job = request.form["job"]
        contract = request.form["contract"]
        city = request.form["city"]
        phone = request.form["phone"]

        # Check if all fields are filled
        if not all([namefile, name, job, contract, city, phone]):
            flash("Please fill out all fields!")
            return redirect(url_for("index"))

        # Generate QR code
        qr_data = f"Employee Name: {name}\nJob Profile: {job}\nContract Type: {contract}\nPhone Number: {phone}\nCity: {city}"
        qr_code = qrcode.make(qr_data)
        qr_path = os.path.join(QR_DIR, f"{namefile}.png")
        qr_code.save(qr_path)

        # Text-to-speech message for confirmation
        engine = pyttsx3.init()
        engine.say("Saved Successfully")
        engine.runAndWait()

        flash(f"QR Code for {namefile} generated successfully!")
        return render_template("index.html", qr_image=qr_path)

    # Play welcome sound when loading the page
    play_audio("static/sounds/welcome.wav")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
