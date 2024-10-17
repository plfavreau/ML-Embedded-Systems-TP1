FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api.py .
COPY regression.joblib .

EXPOSE 8459

CMD ["python", "api.py"]
