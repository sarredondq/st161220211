from pykafka import KafkaClient
client = KafkaClient(hosts="1b-1.st1612-cluster-1.e0djg5.c8.kafka.us-east-1.amazonaws.com:9092")

client.topics
topic = client.topics['my.test']

print(topics)
