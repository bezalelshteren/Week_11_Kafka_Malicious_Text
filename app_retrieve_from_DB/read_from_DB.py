import pandas as pd
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()


class cech_data:
    def __init__(self):
        self.connection = os.getenv("CONNECTION_TO_MONGO")
        self.db_name = os.getenv("DB_NAME")
        self.collection_name = os.getenv("COLLECTION_NAME")
        self.client = pymongo.MongoClient(self.connection)
        self.offset = 0


    def connect_and_read(self):

        my_db = self.client[self.db_name]
        my_coll = my_db[self.collection_name]
        data = my_coll.find().sort("date", -1).skip(self.offset).limit(100).to_list()
        df = pd.DataFrame(data)
        df["_id"] = df["_id"].astype(str)
        df["CreateDate"] = df["CreateDate"].astype(str)
        self.offset += 100
        return df


# cp = cech_data()
# for i in range(2):
#     data = cp.connect_and_read()
#     print(data)