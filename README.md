# Employee App

Employee App is a Flask-based web application for managing employee data. It allows users to generate QR codes with employee details and provides text-to-speech feedback. Additionally, a welcome sound is played each time the application loads.

## Features
- **QR Code Generation**: Create QR codes with employee information including name, job profile, contract type, city, and phone number.
- **Text-to-Speech (TTS)**: Audio confirmation for successful actions using the pyttsx3 library.
- **Welcome Sound**: Play a welcome sound each time the web page is accessed.

## Prerequisites
Make sure to have **Python 3.x** installed on your system.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ichatosha/Employee-Flask
    cd Employee-App
    ```

2. **Install Dependencies**:
    Install all required packages using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    ```bash
    python app.py
    ```
   Access the app at `http://127.0.0.1:5000`.

4. **File Structure**:
    - **app.py**: Main application file.
    - **static/qr_codes**: Directory for saving generated QR codes.
    - **static/sounds**: Directory containing audio files for TTS.

## Usage
- Fill in employee details in the form.
- Click "Save" to generate a QR code and receive audio confirmation.
- The QR code will be displayed on the page.

## Dependencies
All dependencies are listed in `requirements.txt`. They include:
- `Flask`
- `pyttsx3`
- `qrcode`
- `pydub`

## License
MIT License. See [LICENSE](LICENSE) for details.

## Author
Developed by [HESHAM](https://www.linkedin.com/in/ichatosha).
