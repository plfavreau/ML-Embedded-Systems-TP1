# House Price Prediction API

This project provides a FastAPI-based API for predicting house prices based on features such as size, number of bedrooms, and the presence of a garden. The API is containerized using Docker for easy deployment and scalability.

## Project Structure

- `api.py`: FastAPI application with the prediction endpoint
- `model_app.py`: Streamlit web application for model interaction (not used in the API)
- `train_model.py`: Script to train the regression model (not included in the Docker image)
- `regression.joblib`: Trained model file
- `requirements.txt`: Python dependencies
- `Dockerfile`: Instructions for building the Docker image
- `docker-compose.yml`: Docker Compose configuration for easy deployment

## Setup and Installation

1. Clone this repository:   
```
   git clone <repository-url>
   cd house-price-prediction-api
```

3. Ensure you have Docker and Docker Compose installed on your system.

4. Build and run the Docker container:   
```
   docker-compose up -d
```

   This command will build the Docker image and start the container in detached mode.

1. The API will be available at `http://localhost:8000`.

## Using the API

### Swagger UI

You can interact with the API using the Swagger UI:

1. Open a web browser and go to `http://localhost:8000/docs`
2. You'll see the interactive API documentation
3. Expand the `/predict` endpoint
4. Click on "Try it out"
5. Input your test values and execute the request