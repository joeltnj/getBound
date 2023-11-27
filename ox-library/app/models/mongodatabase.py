from pymongo import MongoClient

class MongoDBDatabase:
    def __init__(self, host, port, database):
        self.host = host
        self.port = port
        self.database = database
        self.client = None
        self.db = None
        # self.client = MongoClient(self.host, self.port)
        # self.db = self.client[self.database]

    def connect(self):
        self.client = MongoClient(self.host, self.port)
        self.db = self.client[self.database]

    def check_collection_exists(self, collection_name):
        return collection_name in self.db.list_collection_names()

    def create_users_collection(self):
        if not self.check_collection_exists('lesUsers'):
            self.db.create_collection('lesUsers')

    def close_connection(self):
        if self.client:
            self.client.close()
