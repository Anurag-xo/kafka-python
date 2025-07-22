import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka:9092')

for i in range(100):
    message = f"Message {i}"
    producer.send('my-topic', message.encode('utf-8'))
    print(f"Sent: {message}")
    time.sleep(1)

producer.flush()