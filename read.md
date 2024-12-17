# Audio to Image Application

This application converts audio files to spectrogram images via a simple Flask API.

## Setup

1. Clone the repository.
2. Create a virtual environment and install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python app/app.py
    ```

## API

### POST /upload
Upload an audio file (MP3/WAV) and receive a PNG image of its spectrogram.
