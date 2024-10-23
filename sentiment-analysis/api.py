from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(
    title="Sentiment Analysis API",
    description="This API performs sentiment analysis using a BERT model.",
    version="1.0.0",
)

sentiment_pipeline = pipeline("sentiment-analysis")

class TextData(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": "This is a simple test, ml ops is amazing"
            }
        }

@app.post("/analyze", response_model=dict, summary="Analyze sentiment", description="Analyzes the sentiment of the given text")
async def analyze_sentiment(text_data: TextData):
    """
    Analyze the sentiment of the given text.
    
    Returns the sentiment label and score.
    """
    result = sentiment_pipeline(text_data.text)[0]
    return {"label": result["label"], "score": result["score"]}

@app.get("/", summary="Root", description="Returns a welcome message")
async def root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Sentiment Analysis API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
