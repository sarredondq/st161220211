from kafka import KafkaClient
from kafka import KafkaConsumer

consumer = KafkaConsumer('AWSKafkaTutorialTopic',bootstrap_servers='b-1.st1612-cluster-1.e0djg5.c8.kafka.us-east-1.amazonaws.com:9092')
for message in consumer:
    print (message)
