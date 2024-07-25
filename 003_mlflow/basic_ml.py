import os
import time
import argparse
import numpy as np
import pandas as pd
import mlflow
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error
from sklearn.model_selection import train_test_split


URL = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
TARGET_COL = "quality"


def load_data():
    try:
        return pd.read_csv(URL, sep=";")
    except Exception as e:
        raise e


def eval_function(actual, pred):
    rmse = root_mean_squared_error(actual, pred)
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


def main(alpha, l1_ratio):
    df = load_data()
    y = df[TARGET_COL]
    X = df.drop(columns=[TARGET_COL])
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=6, test_size=0.2)

    mlflow.set_experiment("ML-Model-1")
    with mlflow.start_run():
        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)

        model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=6)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        rmse, mae, r2 = eval_function(y_test, y_pred)

        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2-score", r2)
        mlflow.sklearn.log_model(model, "trained_model") # model and folder name


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--alpha", "-a", type=float, default=0.2)
    args.add_argument("--l1_ratio", "-l1", type=float, default=0.3)
    parsed_args = args.parse_args()
    main(parsed_args.alpha, parsed_args.l1_ratio)
