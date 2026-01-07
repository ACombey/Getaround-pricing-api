from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(
    title="Getaround Pricing API",
    description="API de prédiction de prix pour Getaround",
    version="1.0.0"
)

# Charger le modèle au démarrage
model = joblib.load("models/xgb_pipeline_pricing.pkl")

class CarFeatures(BaseModel):
    model_key: str
    mileage: int
    engine_power: int
    fuel: str
    paint_color: str
    car_type: str
    private_parking_available: bool
    has_gps: bool
    has_air_conditioning: bool
    automatic_car: bool
    has_getaround_connect: bool
    has_speed_regulator: bool
    winter_tires: bool

@app.get("/")
def root():
    return {"message": "Getaround Pricing API - Use /docs for documentation"}

@app.post("/predict")
def predict_price(features: CarFeatures):
    # Convertir en DataFrame
    input_df = pd.DataFrame([features.dict()])
    
    # Prédiction
    prediction = model.predict(input_df)[0]
    
    return {
        "predicted_price": round(float(prediction), 2),
        "currency": "EUR",
        "unit": "per_day"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}