import pytest
import joblib
import pandas as pd
import numpy as np

def test_model_loads():
    model = joblib.load("models/xgb_pipeline_pricing.pkl")
    assert model is not None

def test_model_prediction_shape():
    model = joblib.load("models/xgb_pipeline_pricing.pkl")
    
    test_data = pd.DataFrame([{
        "model_key": "Citroën",
        "mileage": 50000,
        "engine_power": 100,
        "fuel": "diesel",
        "paint_color": "black",
        "car_type": "sedan",
        "private_parking_available": True,
        "has_gps": True,
        "has_air_conditioning": True,
        "automatic_car": False,
        "has_getaround_connect": True,
        "has_speed_regulator": True,
        "winter_tires": False
    }])
    
    prediction = model.predict(test_data)
    assert len(prediction) == 1
    assert isinstance(prediction[0], (int, float, np.number))

def test_model_prediction_range():
    model = joblib.load("models/xgb_pipeline_pricing.pkl")
    
    test_data = pd.DataFrame([{
        "model_key": "Renault",
        "mileage": 80000,
        "engine_power": 120,
        "fuel": "petrol",
        "paint_color": "white",
        "car_type": "convertible",
        "private_parking_available": False,
        "has_gps": False,
        "has_air_conditioning": True,
        "automatic_car": True,
        "has_getaround_connect": False,
        "has_speed_regulator": True,
        "winter_tires": False
    }])
    
    prediction = model.predict(test_data)[0]
    assert 10 <= prediction <= 500