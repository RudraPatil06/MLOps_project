from flask import Flask, request, jsonify
import numpy as np
from src.api.model_loader import load_model  # reuse same model

app = Flask(__name__)

model = load_model()

@app.route("/")
def home():
    return jsonify({"message": "Flask ML Inference Running"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)[0]
    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    app.run(debug=True)