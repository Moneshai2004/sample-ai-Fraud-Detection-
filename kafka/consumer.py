# kafka/consumer.py
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('transactions',
                         bootstrap_servers='localhost:9092',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    transaction = message.value
    print(f"Consumed: {transaction}")
    # Pass transaction to data preprocessing pipeline here
