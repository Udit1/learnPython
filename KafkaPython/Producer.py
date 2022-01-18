from kafka import KafkaProducer
from data import mock_data
import json


def json_serializer(data):
    return json.dumps(data).encode('utf-8')


producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"], value_serializer=json_serializer)

if __name__ == "__main__":
    for i in range(20):
        gen_mock = mock_data()
        producer.send("Test_topic", gen_mock)
        print(gen_mock)
