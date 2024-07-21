import os
import pathlib
import prediction_model


PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent

DATA_PATH = os.path.join(PACKAGE_ROOT, "datasets")

TRAIN_FILE = "train.csv"
TEST_FILE = "test.csv"

MODEL_NAME = "classifier.pkl"
MODEL_SAVE_PATH = os.path.join(PACKAGE_ROOT, "trained_models")

TARGET_COL = "Loan_Status"

#Final features used in the model
FEATURES = [
    "Gender", "Married", "Dependents", "Education",
    "Self_Employed", "ApplicantIncome", "CoapplicantIncome", "LoanAmount",
    "Loan_Amount_Term", "Credit_History", "Property_Area"
]

NUM_FEATURES = [
    "ApplicantIncome", "LoanAmount", "Loan_Amount_Term"
]

CAT_FEATURES = [
    "Gender", "Married", "Dependents", "Education",
    "Self_Employed", "Credit_History", "Property_Area"
]

# same as Categorical features
FEATURES_TO_ENCODE = [
    "Gender", "Married", "Dependents", "Education",
    "Self_Employed", "Credit_History", "Property_Area"
]

FEATURE_TO_MODIFY = ["ApplicantIncome"]
FEATURE_TO_ADD = "CoapplicantIncome"

DROP_FEATURES = ["CoapplicantIncome"]
LOG_FEATURES = ["ApplicantIncome", "LoanAmount"] # taking log of numerical columns