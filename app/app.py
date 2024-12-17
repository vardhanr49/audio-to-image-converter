# app/app.py
from flask import Flask, request, jsonify, send_file
import os
from app.audio_to_image import audio_to_image

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
OUTPUT_FOLDER = 'output_images/'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Endpoint to upload an audio file and get its spectrogram as an image"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        audio_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(audio_path)
        
        output_image = os.path.join(OUTPUT_FOLDER, file.filename + '.png')
        audio_to_image(audio_path, output_image)
        
        return send_file(output_image, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
