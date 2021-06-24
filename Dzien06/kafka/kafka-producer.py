from kafka import KafkaProducer
from datetime import datetime
import time

HOST = "ec2-35-157-249-171.eu-central-1.compute.amazonaws.com"
producer = KafkaProducer(bootstrap_servers=[f"{HOST}:9092"])

for _ in range(10):
    message = f"DATA I CZAS: {datetime.utcnow()}"
    print(message)
    producer.send('mar_wit', message.encode("utf-8"))
    time.sleep(3)

producer.flush()
producer.close()