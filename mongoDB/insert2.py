import json
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.mydb
collection = db.mycollection

index_name = "city_index"
collection.create_index("address.city", name=index_name)

