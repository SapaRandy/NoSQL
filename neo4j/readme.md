Récupérer l'image de Neo4j
`docker pull neo4j`

Démarrer un conteneur 
`docker run\     
    \--name my_neo4j     
    \-p7474:7474 -p7687:7687     
    \-v ~/neo4j_data:/data     
    \-e NEO4J_AUTH=neo4j/password     
    \-d neo4j`