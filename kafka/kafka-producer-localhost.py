from kafka import KafkaProducer
from kafka import KafkaClient

#client = KafkaClient(bootstrap_servers='localhost:9092')
#client.add_topic('sampletopic')

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('sampletopic', b'Hello, World!')
future = producer.send('sampletopic', key=b'message-two', value=b'This is Kafka-Python')
producer.flush()

