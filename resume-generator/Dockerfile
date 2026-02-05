FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY template/ ./template/

VOLUME ["/app/data"]
WORKDIR /app/data

ENTRYPOINT ["python", "/app/src/generate.py"]
