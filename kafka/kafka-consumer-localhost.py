from kafka import KafkaClient
from kafka import KafkaConsumer

consumer = KafkaConsumer('sampletopic',bootstrap_servers='localhost:9092')
for message in consumer:
    print (message)
