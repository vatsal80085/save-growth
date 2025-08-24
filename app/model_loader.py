from tensorflow import keras

# Load once at startup
model = keras.models.load_model("app/plant_disease_recog_model_pwp.keras")

# Modify with your dataset’s classes
class_names = ["Healthy", "Powdery Mildew", "Rust", "Leaf Spot"]
