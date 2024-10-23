# MLOps Project: House Price Prediction and Sentiment Analysis

This project consists of two machine learning services:
1. House Price Prediction
2. Sentiment Analysis

Both services are containerized using Docker and deployed automatically using GitHub Actions.

## House Price Prediction Service

This service predicts house prices based on features like size, number of bedrooms, and presence of a garden.

### API Endpoints

- `POST /predict`: Predicts the price of a house based on input features.

## Sentiment Analysis Service

This service performs sentiment analysis on text using a lightweight DistilBERT model.

### API Endpoints

- `POST /analyze`: Analyzes the sentiment of the given text.
- `GET /`: Returns a welcome message.

## Using the APIs

### House Price Prediction

You can interact with the House Price Prediction API using the Swagger UI:

1. Open a web browser and go to `http:20.86.55.5//:5959/docs`
2. You'll see the interactive API documentation
3. Expand the `/predict` endpoint
4. Click on "Try it out"
5. Input your test values and execute the request

### Sentiment Analysis

To test the Sentiment Analysis API, you can use curl:

```
curl -X POST "http://20.86.55.5:5960/analyze" -H "Content-Type: application/json" -d '{"text": "This is a simple test, ml ops is amazing"}'
```
