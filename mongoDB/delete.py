from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.mydb
collection = db.mycollection

query = {"name": "John Doe"}
result = collection.delete_one(query)
print("Deleted document count:", result.deleted_count)

query = {"age": {"$gt": 25}}
result = collection.delete_many(query)
print("Deleted document count:", result.deleted_count)