from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

#documents to insert in the elasticsearch index "cities"
doc1 = {"city":"New Delhi", "country":"India"}
doc2 = {"city":"London", "country":"England"}
doc3 = {"city":"Los Angeles", "country":"USA"}

#Inserting doc1 in id=1
es.index(index="cities", id=1, body=doc1)

#Inserting doc2 in id=2
es.index(index="cities", id=2, body=doc2)

#Inserting doc3 in id=3
es.index(index="cities", id=3, body=doc3)