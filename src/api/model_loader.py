import os
import joblib

# Get absolute base directory of project
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

MODEL_PATH = os.path.join(BASE_DIR, "artifacts", "model.pkl")

def load_model():
    print("Loading model from:", MODEL_PATH)
    return joblib.load(MODEL_PATH)