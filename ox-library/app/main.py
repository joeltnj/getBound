from pymongo import MongoClient
from models.mongodatabase import MongoDBDatabase

class Main:
    def __init__(self):
        self.mongoclient = MongoClient("localhost",27017)
        self.mongodb=self.mongoclient["myDB"]


    def connexionToBD(self):
        # mongo_config = {"host": "localhost", "port": 27017, "database": "myDB"}
        # self.mongoclient = MongoDBDatabase("localhost",27107)
        # self.mongodb.connect()
        # self.mongodb=self.mongoclient["myDB"]
        
        self.mongodb.create_users_collection()

    # def connexionLogin(self, name, password):
        


 