# Universidad del Valle de Guatemala
# Redes - Seccion 20
# Laboratorio 10 - Kafka
# 19710 - Christian Perez
# 19588 - Marco Ramirez

from kafka import KafkaConsumer
from kafka import TopicPartition
import json


consumer = KafkaConsumer(bootstrap_servers='lab10.alumchat.fun')
consumer.assign([TopicPartition('19588', 0)])

for message in consumer:
    print(json.loads(message.value.decode('utf-8')))
