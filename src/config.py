import os

class ModelTrainerConfig:
    def __init__(self):
        self.model_path = os.path.join("artifacts", "model.pkl")
