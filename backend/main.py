from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import tensorflow as tf
import numpy as np
from PIL import Image
import io

# ==========================================
# Initialize FastAPI
# ==========================================

app = FastAPI()

# ==========================================
# Enable CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# Load Trained Model
# ==========================================

model = tf.keras.models.load_model(
    "model/plant_disease_model_final.keras"
)

# ==========================================
# Class Names
# ==========================================

class_names = [
    "Pepper Bell Bacterial Spot",
    "Pepper Bell Healthy"
]

# ==========================================
# Image Preprocessing Function
# ==========================================

IMG_SIZE = 128

def preprocess_image(image):

    image = image.resize((IMG_SIZE, IMG_SIZE))

    image = np.array(image)

    image = image / 255.0

    image = np.expand_dims(image, axis=0)

    return image

# ==========================================
# Home Route
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Plant Disease Detection API Running"
    }

# ==========================================
# Prediction Route
# ==========================================

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    image_bytes = await file.read()

    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    processed_image = preprocess_image(image)

    prediction = model.predict(processed_image)

    predicted_index = np.argmax(prediction)

    confidence = float(np.max(prediction))

    predicted_class = class_names[predicted_index]

    return {
        "predicted_class": predicted_class,
        "confidence": round(confidence * 100, 2)

    }


