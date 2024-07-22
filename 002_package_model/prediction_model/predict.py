import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset, load_pipeline


classification_pipeline = load_pipeline()


def make_predictions(data_input):
    data = pd.DataFrame(data_input)
    pred = classification_pipeline.predict(data[config.FEATURES])
    output = np.where(pred==1, "Y", "N")
    return {"prediction": output}


def generate_predictions():
    test_data = load_dataset(config.TEST_FILE)
    pred = classification_pipeline.predict(test_data[config.FEATURES])
    output = np.where(pred==1, "Y", "N")
    print(output)
    return output


if __name__ == "__main__":
    generate_predictions()
