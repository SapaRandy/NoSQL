from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.mydb
collection = db.mycollection

query = {"name": "John Doe"}
document = collection.find_one(query)
print(document)

query = {"age": {"$gt": 25}}
documents = collection.find(query)

for doc in documents:
    print(doc)