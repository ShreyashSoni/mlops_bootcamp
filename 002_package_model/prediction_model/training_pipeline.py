import os
import sys
from pathlib import Path

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

import prediction_model.pipeline as pipe
from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset, save_pipeline


def perform_training():
    train_data = load_dataset(config.TRAIN_FILE)
    train_y = train_data[config.TARGET_COL].map({"N": 0, "Y": 1})
    pipe.classification_pipeline.fit(train_data[config.FEATURES], train_y)
    save_pipeline(pipe.classification_pipeline)


if __name__ == "__main__":
    perform_training()
