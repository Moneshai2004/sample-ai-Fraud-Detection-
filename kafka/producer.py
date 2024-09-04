# kafka/producer.py
from kafka import KafkaProducer
import json
import time
import random

def generate_transaction():
    return {
        'transaction_id': random.randint(10000, 99999),
        'user_id': random.randint(1, 1000),
        'amount': round(random.uniform(1.0, 1000.0), 2),
        'timestamp': int(time.time()),
        'location': random.choice(['New York', 'London', 'Paris', 'Tokyo']),
        'merchant': random.choice(['Amazon', 'Walmart', 'Target'])
    }

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    transaction = generate_transaction()
    producer.send('transactions', transaction)
    print(f"Produced: {transaction}")
    time.sleep(1)
