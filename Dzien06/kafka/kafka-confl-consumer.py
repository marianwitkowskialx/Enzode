from confluent_kafka import Consumer
from datetime import datetime
import time

HOST = "ec2-35-157-249-171.eu-central-1.compute.amazonaws.com"
consumer = Consumer({
    'bootstrap.servers' : f"{HOST}:9092",
    'group.id' : "my-group",
    'enable.auto.commit' : False
})

consumer.subscribe(["mar_wit"])
while True:
    msg = consumer.poll(1.5)
    if msg is None:
        continue
    print(msg.value())
    consumer.commit(msg)