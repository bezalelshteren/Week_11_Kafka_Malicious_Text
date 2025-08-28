import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

class Get_data:
    def __init__(self, col_name, uri=None, db_name=None):
        self.uri = uri or os.getenv("MONGO_CONN")
        if not self.uri:
            raise ValueError("MONGO_CONN missing")
        self.client = pymongo.MongoClient(self.uri)
        self.db = self.client[db_name or os.getenv("MONGO_DB", "iran")]
        self.col = self.db[col_name]