from neo4j import GraphDatabase

uri = "bolt://localhost:7687"

user = "neo4j"
password = "password"

driver = GraphDatabase.driver(uri, auth=(user, password))

def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return result
    
query_all_persons = "MATCH (p:Person) RETURN p.name, p.age"

results = run_query(query_all_persons)

for record in results:
    print(f"Name: {record['p.name']}, Age: {record['p.age']}")

def get_friends(name):
    query = f"MATCH (p:Person {{name: '{name}'}})-[:FRIEND]->(friend) RETURN friend.name, friend.age"
    results = run_query(query)
    return results

name = "Alice"
friends = get_friends(name)

print(f"Friends of {name}:")
for record in friends:
    print(f"Name: {record['friend.name']}, Age: {record['friend.age']}")