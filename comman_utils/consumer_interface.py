from kafka import KafkaConsumer
from dotenv import load_dotenv
import os
import json

load_dotenv()

topic_clean_antisemitic = os.getenv("TOPIC_CLEAN_ANTISEMITIC")
topic_clean_not_antisemitic = os.getenv("TOPIC_CLEAN_NOT_ANTISEMITIC")
group_clean = os.getenv("GROUP_NAME","interest_group")

class Consumer:
    def __init__(self,not_antisemitic,antisemitic,group):#group
        self.topic_not_antisemitic = not_antisemitic
        self.topic_antisemitic = antisemitic
        self.group_name = group


    def get_consumer_events(self):
        consumer = KafkaConsumer(
            self.topic_antisemitic,self.topic_not_antisemitic,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            bootstrap_servers=['localhost:9092'],
            consumer_timeout_ms=10000,
            auto_offset_reset='earliest',
            group_id=self.group_name
        )

        return consumer
#
# p = Consumer(topic_clean_not_antisemitic,topic_clean_antisemitic,group_clean)
# o = p.get_consumer_events()

# for msg in o:
#     print(type(msg.value),f"value={msg.value}")
