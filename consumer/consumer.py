from kafka import KafkaConsumer
import json
import numpy as np
from dotenv import load_dotenv
import os
import sys 

load_dotenv()

topic = os.getenv("TOPIC_NAME")

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
    value_deserializer=lambda v: np.array(json.loads(v.decode('utf-8'))),
    auto_offset_reset='earliest',  
    enable_auto_commit=True,
    auto_commit_interval_ms=500,  # Réduit le temps d’attente avant le commit
    consumer_timeout_ms=5000  # Attend 5s avant de quitter s'il n'y a pas de message
)

for message in consumer:
    array = message.value
    print(f"Consumer: Tableau reçu - {array}")
    sys.stdout.flush()  # Force l'affichage des logs
