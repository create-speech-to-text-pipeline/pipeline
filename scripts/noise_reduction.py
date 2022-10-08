import urllib.request
import io
import IPython
import soundfile as sf
import librosa
from tempfile import SpooledTemporaryFile
import noisereduce as nr
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

def remove_noise(audio_data):
    audio, sr = librosa.load(audio_data, sr=8000, mono=True)
    clean_audio = nr.reduce_noise(audio_data, sr=sr,
                                  n_std_thresh_stationary=1.5, stationary=True)

    return clean_audio

def remove_silence(audio_data):
    audio, sr = librosa.load(audio_data, sr=8000, mono=True)
    clips = librosa.effects.split(audio, top_db=10)
    wav_data = []
    for c in clips:
        data = audio[c[0]: c[1]]
        wav_data.extend(data)
    return wav_data