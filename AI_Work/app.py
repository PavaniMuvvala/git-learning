from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Sentiment Service")

class TextPayload(BaseModel):
    text: str

def analyze_sentiment(text: str) -> str:
    """Mock ML inference logic."""
    lowered = text.lower()
    if any(word in lowered for word in ["great", "awesome", "fast", "love"]):
        return "positive"
    elif any(word in lowered for word in ["bad", "terrible", "slow", "hate"]):
        return "negative"
    return "neutral"

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
def predict_sentiment(payload: TextPayload):
    sentiment = analyze_sentiment(payload.text)
    return {"text": payload.text, "sentiment": sentiment}