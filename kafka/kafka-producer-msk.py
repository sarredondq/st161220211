from kafka import KafkaProducer
from kafka import KafkaClient

client = KafkaClient(bootstrap_servers='b-1.st1612-cluster-1.e0djg5.c8.kafka.us-east-1.amazonaws.com:9092')
client.add_topic('AWSKafkaTutorialTopic')

producer = KafkaProducer(bootstrap_servers='b-1.st1612-cluster-1.e0djg5.c8.kafka.us-east-1.amazonaws.com:9092')
print(producer.send('AWSKafkaTutorialTopic', b'Hello, World!'))
producer.send('AWSKafkaTutorialTopic', key=b'message-two', value=b'This is Kafka-Python')

