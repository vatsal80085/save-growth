from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from tensorflow import keras
import numpy as np
from PIL import Image
import io

from model_loader import model, class_names

app = FastAPI(title="Plant Disease Detection API")

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Read image
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).resize((224, 224))  # adjust input size
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Make prediction
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]
    confidence = float(np.max(predictions))

    return JSONResponse({
        "class": predicted_class,
        "confidence": confidence
    })
