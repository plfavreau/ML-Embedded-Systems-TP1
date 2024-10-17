from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(
    title="House Price Prediction API",
    description="This API predicts house prices based on size, number of bedrooms, and garden presence.",
    version="1.0.0",
)

model = joblib.load("regression.joblib")

class HouseData(BaseModel):
    size: float
    bedrooms: int
    has_garden: int

    class Config:
        schema_extra = {
            "example": {
                "size": 1500.0,
                "bedrooms": 3,
                "has_garden": 1
            }
        }

@app.post("/predict", response_model=dict, summary="Predict house price", description="Predicts the price of a house based on its features")
async def predict(house_data: HouseData):
    """
    Predict the price of a house based on the following features:
    
    - **size**: Size of the house in square feet
    - **bedrooms**: Number of bedrooms
    - **has_garden**: Whether the house has a garden (0 for No, 1 for Yes)
    
    Returns the predicted price of the house.
    """
    input_data = [[house_data.size, house_data.bedrooms, house_data.has_garden]]
    prediction = model.predict(input_data)
    return {"predicted_price": round(prediction[0], 2)}

@app.get("/", summary="Root", description="Returns a welcome message")
async def root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the House Price Prediction API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
