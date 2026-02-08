import sys
from src.logger import logging
from src.exception import CustomException

from src.components.model_trainer import ModelTrainer
from src.components.data_transformation import DataTransformation


def run_training_pipeline():
    try:
        logging.info("Starting Training Pipeline")

        train_path = "artifacts/train.csv"
        test_path = "artifacts/test.csv"

        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
            train_path, test_path
        )

        logging.info("Data transformation completed")

        model_trainer = ModelTrainer()

        score = model_trainer.initiate_model_trainer(
            train_array=train_arr,     # <-- changed
            test_array=test_arr,       # <-- changed
            model_path="artifacts/model.pkl"
        )

        logging.info(f"Training completed. Model score: {score}")

    except Exception as e:
        raise CustomException(e, sys)


if __name__ == "__main__":
    run_training_pipeline()
