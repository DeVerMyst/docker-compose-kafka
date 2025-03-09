FROM python:3.9-slim

WORKDIR /app  # Assure un répertoire de travail

RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["./wait-for-kafka.sh", "python", "producer.py"]
