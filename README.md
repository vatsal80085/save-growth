# save-growth
Running Locally
# Build image
docker build -t plant-disease-api .

# Run container
docker run -p 8000:8000 plant-disease-api


Then go to:
👉 http://localhost:8000/docs
 to test Swagger UI.

## This project provides a FastAPI backend that uses a pre-trained Keras model (xyz.keras) to detect plant diseases from leaf images.
It is fully containerized with Docker, so anyone can run it easily.

📂 Project Structure
plant-disease-detection/
│── app/
│   ├── main.py          # FastAPI backend
│   ├── model_loader.py  # Loads keras model + class names
│   ├── requirements.txt # Dependencies
│   └── xyz.keras        # Pre-trained model
│
│── Dockerfile
│── .dockerignore
│── README.md


 1. Clone the Repo
git clone https://github.com/<your-username>/plant-disease-detection.git
cd plant-disease-detection

2. Run Locally (without Docker)

Make sure Python 3.9+ is installed.

cd app
pip install -r requirements.txt
uvicorn main:app --reload


Go to 👉 http://127.0.0.1:8000/docs
 to test.

3. Run with Docker 🐳
# Build image
docker build -t plant-disease-api .

# Run container
docker run -p 8000:8000 plant-disease-api


Now the API will be available at:
👉 http://localhost:8000

Swagger docs:
👉 http://localhost:8000/docs

📡 API Usage
Endpoint: POST /predict/

Accepts an image file (leaf image).

Returns predicted class and confidence.

Request Example (using curl):

curl -X POST "http://127.0.0.1:8000/predict/" \
-F "file=@sample_leaf.jpg"


Response Example:

{
  "class": "Powdery Mildew",
  "confidence": 0.92
}

## 👨‍💻 For Teammates

##    Add UI (React, Vue, etc.) → Call /predict/ API.

##    Extend model_loader.py → Update class_names as per dataset.

##    Add authentication/logging if needed.

##    Set up CI/CD (GitHub Actions, AWS, etc.) for deployment.

🛠 Tech Stack

FastAPI – Web framework

TensorFlow/Keras – ML model

Docker – Containerization

Uvicorn – ASGI server

