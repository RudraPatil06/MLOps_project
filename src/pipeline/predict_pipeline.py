import os
import sys
import pandas as pd

from src.utils import load_object
from src.exception import CustomException
from src.logger import logging


def run_prediction_pipeline():
    try:
        # Load preprocessor and model
        preprocessor = load_object("artifacts/preprocessor.pkl")
        model = load_object("artifacts/model.pkl")

        # Load test data
        test_df = pd.read_csv("artifacts/test.csv")

        # Split features and target
        X = test_df.drop(columns=["math_score"])
        y = test_df["math_score"]

        # Transform features
        X_transformed = preprocessor.transform(X)

        # Predict
        y_pred = model.predict(X_transformed)

        # Save predictions
        result_df = pd.DataFrame({"Actual": y, "Predicted": y_pred})
        result_df.to_csv("artifacts/predictions.csv", index=False)

        logging.info("Prediction completed and saved at artifacts/predictions.csv")
        return result_df

    except Exception as e:
        raise CustomException(e, sys)


if __name__ == "__main__":
    result = run_prediction_pipeline()
    print(result.head())
