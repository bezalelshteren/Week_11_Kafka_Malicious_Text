from comman_utils.consumer_interface import Consumer
from app_write_to_mongo.mongo_writer import MongoWriter
import os
from dotenv import load_dotenv

load_dotenv()




class Manager:
    topic_read1 = os.getenv("TOPIC_TO_MONGO_ANTI","antisemitic")
    topic_read2 =  os.getenv("TOPIC_TO_MONGO_NOT_ANTI","not_antisemitic")
    group = os.getenv("GROUP_TO_MONGO","to_mongo")

    def __init__(self):
        self.consumer =Consumer(self.topic_read1,self.topic_read2,self.group)
        self.writer_anti = MongoWriter(self.topic_read1)
        self.writer_not_anti = MongoWriter(self.topic_read2)

    def start_loop(self):
        for msg in self.consumer.get_consumer_events():
            try:
                if msg.topic == self.topic_read1:
                    self.writer_anti.insert_event(msg)
                    print("s")
                elif msg.topic  == self.topic_read2:
                    self.writer_not_anti.insert_event(msg)
                    print("a")
            except Exception as e:
                print(f"faild to write to mongo{e}")



a = Manager()
a.start_loop()
