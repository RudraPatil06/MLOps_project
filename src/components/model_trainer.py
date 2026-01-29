import os
import sys
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

from src.logger import logging
from src.exception import CustomException


class ModelTrainer:
    def __init__(self):
        self.model_path = os.path.join("artifacts", "model.pkl")

    def initiate_model_trainer(self, train_arr, test_arr):
        try:
            X_train, y_train = train_arr[:, :-1], train_arr[:, -1]
            X_test, y_test = test_arr[:, :-1], test_arr[:, -1]

            model = LinearRegression()
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)
            score = r2_score(y_test, y_pred)

            joblib.dump(model, self.model_path)

            logging.info(f"Model saved at {self.model_path}")
            logging.info(f"R2 score: {score}")

            return score

        except Exception as e:
            raise CustomException(e)
