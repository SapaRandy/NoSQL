from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

print(es.indices.analyze(index="french",body={
  "text" : "Je dois bosser pour mon QCM sinon je vais avoir une sale note :( ..."
}))