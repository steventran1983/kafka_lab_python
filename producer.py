import json
from pykafka import KafkaClient

with open("json.txt","r") as file:
    data = json.load(file)

client = KafkaClient(hosts="127.0.0.1:9092")
topic = client.topics["interview"]

with topic.get_sync_producer() as producer:
    for line in data["stationBeanList"]:
        message = json.dumps(line)
        producer.produce(data.encode(encoding="UTF-8"))
