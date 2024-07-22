import os
import sys
import pytest
from pathlib import Path

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset
from prediction_model.predict import make_predictions

# output from predict script not null
# output from predict script is str data type
# the output is Y for an example data

#Fixtures --> functions before test function --> ensure single_prediction

@pytest.fixture
def single_prediction():
    test_data = load_dataset(config.TEST_FILE)
    test_row = test_data[:1]
    return make_predictions(test_row)


def test_single_pred_not_none(single_prediction):
    assert single_prediction is not None


def test_single_pred_str_type(single_prediction):
    assert isinstance(single_prediction.get("prediction")[0], str)


def test_single_pred_validate(single_prediction):
    assert single_prediction.get("prediction")[0] == "Y"