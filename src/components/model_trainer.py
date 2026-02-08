import sys
import dill
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging


class ModelTrainer:
    def __init__(self):
        pass

    def initiate_model_trainer(self, train_array, test_array, model_path):
        try:
            logging.info("Model training started")

            X_train, y_train = train_array[:, :-1], train_array[:, -1]
            X_test, y_test = test_array[:, :-1], test_array[:, -1]

            model = LinearRegression()
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)
            r2 = r2_score(y_test, y_pred)
            logging.info(f"Model R2 score: {r2}")

            # Save model
            with open(model_path, "wb") as f:
                dill.dump(model, f)

            return r2

        except Exception as e:
            raise CustomException(e, sys)
