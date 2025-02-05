import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.mydb
collection = db.mycollection

query = {"age": {"$gt": 25}}
documents = collection.find(query).sort("name", pymongo.ASCENDING)

for doc in documents:
    print(doc)