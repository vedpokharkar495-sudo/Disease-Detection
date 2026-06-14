# Plant Disease Detection System

A Deep Learning based Plant Disease Detection System using CNN, FastAPI, Streamlit, and Docker.

---

# Project Overview

This project detects diseases in pepper bell plant leaves using a Convolutional Neural Network (CNN).

The model classifies plant leaf images into:

* Pepper Bell Bacterial Spot
* Pepper Bell Healthy

---

# Features

* CNN-based image classification
* FastAPI backend API
* Streamlit frontend UI
* Dockerized deployment
* Real-time prediction
* Upload leaf image and detect disease
* High accuracy model (~99%)

---

# Tech Stack

* Python
* TensorFlow / Keras
* CNN
* FastAPI
* Streamlit
* Docker
* OpenCV
* NumPy
* Matplotlib

---

# Project Structure

```bash
Plant_Disease_Detection
|
|---- backend
|       |
|       |---- model
|       |       |---- plant_disease_model_final.keras
|       |
|       |---- main.py
|       |---- Dockerfile
|
|---- frontend
|       |
|       |---- app.py
|       |---- Dockerfile
|
|---- requirements.txt
|
|---- docker-compose.yml
|
|---- README.md
```

---

# ⚙Installation

## 1. Clone Repository

```bash
git clone <repository_url>
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Backend

```bash
cd backend
uvicorn main:app --reload
```

Backend runs on:

```bash
http://localhost:8000
```

Swagger Docs:

```bash
http://localhost:8000/docs
```

---

# Run Frontend

```bash
cd frontend
streamlit run app.py
```

Frontend runs on:

```bash
http://localhost:8501
```

---

# Docker Setup

## Build Containers

```bash
docker-compose build
```

## Run Containers

```bash
docker-compose up
```

---

# Model Details

* Model Type: Custom CNN
* Image Size: 128x128
* Framework: TensorFlow/Keras
* Validation Accuracy: ~99%

---

# Dataset

Dataset used:

PlantVillage Dataset

Classes:

* Pepper Bell Bacterial Spot
* Pepper Bell Healthy

---

# Future Improvements

* Transfer Learning
* Multi-class disease detection
* Mobile app deployment
* Grad-CAM visualization
* Cloud deployment
* Real-time camera prediction

---

# Author

Ved Pokharkar

Machine Learning & Data Science Enthusiast
