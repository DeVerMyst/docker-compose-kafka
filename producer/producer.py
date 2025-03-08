import time
import numpy as np
from kafka import KafkaProducer
import json
from dotenv import load_dotenv
import os

load_dotenv()

producer = KafkaProducer(
    bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
    value_serializer=lambda v: json.dumps(v.tolist()).encode('utf-8')
)

N = int(os.getenv("ARRAY_SIZE"))
topic = os.getenv("TOPIC_NAME")
sleep_time = int(os.getenv("SLEEP_TIME"))

while True:
    array = np.random.rand(N, N)
    producer.send(topic, array)
    print(f"Producer: Tableau envoyé - {array.tolist()}")
    time.sleep(sleep_time)