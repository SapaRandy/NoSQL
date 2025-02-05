from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.mydb
collection = db.mycollection

query = {"age": {"$gt": 25}}
projection = {"_id": 0, "name": 1, "email": 1}
documents = collection.find(query, projection)

for doc in documents:
    print(doc)