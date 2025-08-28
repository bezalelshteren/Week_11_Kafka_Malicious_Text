from cat_data_by_antisemitic import Cat_data_by_antisemitic
from comman_utils.producer_interface import Producer
from read_from_DB import cech_data
import os
from dotenv import load_dotenv
import time

load_dotenv()

class Manager:
    def __init__(self):
        self.read_from_db = cech_data()
        self.cat_the_data = Cat_data_by_antisemitic()
        self.produser = Producer()
        self.topic_antisemitic = os.getenv("TOPIC_ANTISEMITIC")
        self.topic_not_antisemitic = os.getenv("TOPIC_NOT_ANTISEMITIC")


    def start_all_presses(self):
        data = self.read_from_db.connect_and_read()
        antisemitic,not_antisemitic = self.cat_the_data.cat_data(data)

        for index, message in antisemitic.iterrows():
            msg_anti = message.to_dict()
            print(msg_anti)
            self.produser.publish_message(self.topic_antisemitic,msg_anti)
        for index, message in not_antisemitic.iterrows():
            msg_not_anti = message.to_dict()
            print(msg_not_anti)
            self.produser.publish_message(self.topic_not_antisemitic,msg_not_anti)
        return {"send the data":"successfully"}


manager = Manager()
while True:
    time.sleep(60)
    manager.start_all_presses()