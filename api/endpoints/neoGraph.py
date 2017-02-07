
import falcon, json, requests
from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://192.168.99.100/:7687/", auth=basic_auth("neo4j", "Wolf3105"))

class NeoGraphDb:
    """docstring for MainHandler"""
    def on_get(self, req, resp,lbl="", ref=""):
        try:
            # SEARCH QUERY
            session = driver.session()
            if ref == "":
                qry1 = 'MATCH (a:{})  RETURN a.title AS name, a.ref AS reg, a.desc as desc'.format(lbl.upper())
            else:
                qry1 = 'MATCH (a:{}) where a.ref={} RETURN a.title AS name, a.ref AS reg, a.desc as desc'.format( lbl.upper(), ref)

            result = session.run(qry1)

            listr = []
            for record in result:
                print("{}  :  {} : {}".format(record["name"], record["reg"], record["desc"]))
                listr.append([record["name"], record["reg"], record["desc"]])
            session.close()

            resp.body = json.dumps({"Success": "FALCON_GET", "List": listr})
            resp.body = resp.body.encode('utf-8')
            resp.status = falcon.HTTP_200

        except  requests.exceptions.HTTPError as e:
            print (e)
            resp.body = "error : " + str(e)