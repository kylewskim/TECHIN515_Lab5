from flask import Flask, request, jsonify
from tensorflow import keras
import tensorflow as tf
import numpy as np
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

def load_legacy_model(model_path):
    try:
        model = keras.Sequential([
            keras.layers.Input(shape=(300,)),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(2, activation='softmax')
        ])
        
        # Load the weights directly
        model.load_weights(model_path)
        logger.info("Model weights loaded successfully")
        return model
    except Exception as e:
        logger.error(f"Custom model loading error: {str(e)}")
        raise

# Load model once at startup
try:
    model_path = os.path.join(os.getcwd(), "wand_model.h5")
    logger.info(f"Loading model from {model_path}")
    model = load_legacy_model(model_path)
    logger.info("Model loaded successfully")
    model.summary()
except Exception as e:
    logger.error(f"Error loading model: {str(e)}")
    raise

# Update gesture labels to match model output
gesture_labels = ["V", "O"]  # Reduced to 2 classes based on error message

@app.route("/", methods=["GET"])
def home():
    return "Wand Gesture API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json.get("data")
        if not data:
            raise ValueError("Missing 'data' field")

        # 입력 데이터 전처리
        input_array = np.array(data, dtype=np.float32)
        if len(input_array.shape) == 2 and input_array.shape[1] == 300:
            input_array = input_array  # 이미 올바른 shape
        else:
            input_array = input_array.reshape(-1, 300)  # reshape to (batch_size, 300)

        # 예측 수행
        prediction = model.predict(input_array)
        
        # 결과 처리
        top_index = int(np.argmax(prediction))
        label = gesture_labels[top_index]
        confidence = float(prediction[0][top_index]) * 100

        return jsonify({
            "gesture": label,
            "confidence": confidence
        })

    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)