from __future__ import print_function

from neomodel import db, change_neo4j_password, clear_neo4j_database
from neo4j.exceptions import ClientError as CypherError

# Travis default password dance
try:


    change_neo4j_password(db, '0000')
    db.set_connection('bolt://neo4j:0000@localhost:7687')
except CypherError as ce:
    print("Error on PW change or connectiom", str(ce))
    print("Please 'export NEO4J_BOLT_URL=bolt://neo4j:0000@localhost:7687' for test runs")
