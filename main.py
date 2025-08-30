from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI(title="Sentiment Analysis API", version="1.0")

# Load Hugging Face sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Request model
class TextInput(BaseModel):
    text: str

# Health check endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analysis API 🚀"}

# Sentiment analysis endpoint
@app.post("/analyze/")
def analyze_sentiment(input: TextInput):
    result = sentiment_pipeline(input.text)[0]
    return {
        "text": input.text,
        "label": result["label"],
        "score": round(result["score"], 4)
    }
