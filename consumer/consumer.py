from kafka import KafkaConsumer
import json
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()

topic = os.getenv("TOPIC_NAME")

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
    value_deserializer=lambda v: np.array(json.loads(v.decode('utf-8')))
)

for message in consumer:
    array = message.value
    print(f"Consumer: Tableau reçu - {array}")