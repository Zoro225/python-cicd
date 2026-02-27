# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Run tests as part of image build
RUN pytest

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.app:app"]
