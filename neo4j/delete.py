from neo4j import GraphDatabase

uri = "bolt://localhost:7687"

user = "neo4j"
password = "password"

driver = GraphDatabase.driver(uri, auth=(user, password))

def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return result

delete_nodes_and_relationships = "MATCH (n) DETACH DELETE n"
run_query(delete_nodes_and_relationships)