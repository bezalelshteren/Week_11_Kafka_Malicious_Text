from kafka import KafkaConsumer
from dotenv import load_dotenv
from comman_utils.consumer_interface import Consumer
from app_clear_text.processor import TextProcessor
from comman_utils.producer_interface import Producer

import os



load_dotenv()


class Manager:
    topic_read1 = os.getenv("TOPIC_ANTISEMITIC", "row_tweets_not_antisemitic")
    topic_read2 =os.getenv("TOPIC_NOT_ANTISEMITIC","row_tweets_antisemitic")
    group = os.getenv("GROUP_NAME_FIRST","antisemitic_not_antisemitic")

    topic_send1 =os.getenv("TOPIC_CLEAN_ANTISEMITIC")
    topic_send2 =os.getenv("TOPIC_CLEAN_NOT_ANTISEMITIC")
    def __init__(self):
        self.consumer = Consumer(self.topic_read1,self.topic_read2,self.group)
        self.producer = Producer()


    def start_loop(self):
        for msg in self.consumer.get_consumer_events():
            print(type(msg.value),f"value={msg.value}")
            processor = TextProcessor(msg.value["text"])
            cleaned_text = processor.process_all_and_get()
            msg.value["cleaned_text"] = cleaned_text
            if msg.topic == self.topic_read1:
                producer_topic = self.topic_send1
            elif msg.topic  == self.topic_read2:
                producer_topic = self.topic_send2
            else:
                continue
            self.producer.publish_message(producer_topic,msg.value)
            print(msg.value)
            print(f"Message sent to topic {producer_topic}")





a= Manager()
a.start_loop()




