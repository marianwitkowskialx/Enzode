from kafka import KafkaConsumer
from datetime import datetime
import time

HOST = "ec2-35-157-249-171.eu-central-1.compute.amazonaws.com"
consumer = KafkaConsumer(
    "mar_wit",
    bootstrap_servers=[f"{HOST}:9092"],
    auto_offset_reset="earliest",
    group_id = "mar_wit_group",
    enable_auto_commit=False
)

for message in consumer:
    print(message.value)
    consumer.commit()


