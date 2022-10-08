import os
import sys
import glob
import pandas as pd
import numpy as np
import boto3
from botocore.exceptions import ClientError
from scipy.io.wavfile import read


class AudioToArray():
    def __init__(self) -> None:
        pass
    def convert_to_ndarray(path):
        wavs = []
        for filename in glob.glob(path + "wav/*.wav"):
            wavs.append(read(filename))
        return wavs
    def upload_ndarray(file_name: str, bucket='/mnt/10ac-batch-6/bucket/', object_name=None):
        if object_name is None:
            object_name = os.path.basename(file_name)        
        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            print(e)
            return False   
        return True     
    