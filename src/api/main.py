from fastapi import FastAPI
from src.api.schema import PredictionRequest, PredictionResponse
from src.api.model_loader import load_model
import numpy as np

app = FastAPI(title="ML Inference API")

model = load_model()

@app.get("/")
def home():
    return {"message": "FastAPI ML Inference Running"}

@app.post("/predict", response_model=PredictionResponse)
def predict(data: PredictionRequest):
    features = np.array(data.features).reshape(1, -1)
    prediction = model.predict(features)[0]
    return PredictionResponse(prediction=int(prediction))