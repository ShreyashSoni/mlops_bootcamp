import mlflow
logged_model = 'runs:/bc4fba16f1654f0aa6e70a9658a3c128/RandomForestClassifier'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
import pandas as pd

data = [[
    1.0,
    0.0,
    0.0,
    0.0,
    0.0,
    4.98745,
    360.0,
    1.0,
    2.0,
    8.698
]]

print(f"Predictions: {loaded_model.predict(pd.DataFrame(data))}")