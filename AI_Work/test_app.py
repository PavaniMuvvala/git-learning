# test_app.py
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_predict_positive():
    response = client.post("/predict", json={"text": "This model is awesome and fast"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "positive"

def test_predict_negative():
    response = client.post("/predict", json={"text": "This response is terrible"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "negative"