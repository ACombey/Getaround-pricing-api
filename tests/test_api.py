import pytest
from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_predict_endpoint():
    test_data = {
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
    }
    
    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    assert "predicted_price" in response.json()
    assert response.json()["predicted_price"] > 0

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    