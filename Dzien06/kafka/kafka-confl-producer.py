from confluent_kafka import Producer
from datetime import datetime
import time

HOST = "ec2-35-157-249-171.eu-central-1.compute.amazonaws.com"
producer = Producer({
    'bootstrap.servers' : f"{HOST}:9092"
})

for _ in range(10):
    message = f"CURR TIME/DATE: {datetime.utcnow()}"
    print(message)
    producer.produce('mar_wit', message.encode("utf-8"))
    time.sleep(3)

producer.flush()