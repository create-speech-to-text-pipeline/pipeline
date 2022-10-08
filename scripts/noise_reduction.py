import urllib.request
import io
import IPython
import soundfile as sf
import matplotlib.pyplot as plt
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