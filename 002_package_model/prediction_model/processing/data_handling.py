import os
import sys
import joblib
import pandas as pd
from pathlib import Path

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config


# Load the data
def load_dataset(file_name):
    filepath = os.path.join(config.DATA_PATH, file_name)
    return pd.read_csv(filepath)


# Serialization
def save_pipeline(pipeline_to_save):
    save_path = os.path.join(config.MODEL_SAVE_PATH, config.MODEL_NAME)
    joblib.dump(pipeline_to_save, save_path)
    print(f"Model saved by the name {config.MODEL_NAME}...")


# Deserialization
def load_pipeline():
    pipeline_path = os.path.join(config.MODEL_SAVE_PATH, config.MODEL_NAME)
    model = joblib.load(pipeline_path)
    print("Model successfully loaded...")
    return model