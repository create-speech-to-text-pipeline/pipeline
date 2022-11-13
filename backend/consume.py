import json
from time import sleep

from kafka import KafkaConsumer

def consume():
    consumer = KafkaConsumer(
        'quickstart-events',
        auto_offset_reset='earliest',
        bootstrap_servers=['localhost:9092'],
        api_version=(0, 10),
        consumer_timeout_ms=1000
    )
    

    for msg in consumer:
        print(msg.value)

    if consumer is not None:
        consumer.close()