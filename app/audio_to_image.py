# app/audio_to_image.py
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import os

def audio_to_image(audio_file, output_image):
    """Converts an audio file to a spectrogram image"""
    # Load the audio file
    y, sr = librosa.load(audio_file, sr=None)

    # Generate the spectrogram
    S = librosa.stft(y)  # Short-time Fourier transform
    S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)

    # Create the plot
    plt.figure(figsize=(10, 6))
    librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(label='Amplitude (dB)')
    plt.title('Spectrogram')

    # Save the image to a file
    plt.savefig(output_image, bbox_inches='tight')
    plt.close()

    return output_image
