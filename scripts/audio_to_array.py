import os
import sys
import glob
import pandas as pd
import numpy as np
import boto3
from botocore.exceptions import ClientError
from scipy.io.wavfile import read