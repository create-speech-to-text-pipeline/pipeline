import os
import wave

def extract_sample_rate(path):
    for file_name in os.listdir(path):
        with wave.open(file_name, "rb") as wave_file:
            frame_rate = wave_file.getframerate()
    return frame_rate