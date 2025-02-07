import requests
from elasticsearch import Elasticsearch

res = requests.get('http://localhost:9200?pretty')
print(res.content)

es = Elasticsearch('http://localhost:9200')
