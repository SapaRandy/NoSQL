import json
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.mydb
collection = db.mycollection

city = "Bradshawborough"
results = collection.find({"address.city": city})

for result in results:
    print(result)
    
min_balance = 30000
results = collection.find({"balance": {"$gt": min_balance}})

for result in results:
    print(result)

pipeline = [
    {"$group": {"_id": "$address.city", "total_balance": {"$sum": "$balance"}}},
    {"$sort": {"total_balance": -1}}
]

results = collection.aggregate(pipeline)

for result in results:
    print(f"{result['_id']}: {result['total_balance']}")