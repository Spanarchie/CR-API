
import json, falcon
import requests
from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://192.168.99.100/:7687/", auth=basic_auth("neo4j", "Wolf3105"))


class NeoGraphDb:
    """docstring for MainHandler"""
    listr = []

    def on_get(self, req, resp, lbl="", ref=""):
        try:
            self.cyphergraph(lbl, ref)
            data = "Hello Welcome to Docker -> NEO -> Falcon \n {}".format(self.listr)
            resp.body = data
        except  requests.exceptions.HTTPError as e:
            print (e)
            resp.body = "error : " + str(e)

    def on_post(self, req, resp):
        try:
            data = req.stream.read()
            info = json.loads(data.decode("utf-8"))

            print("Info = {}".format(info))
            self.postgraph(info)

            resp.body = "Post Successful - {}".format(self.listr)
            resp.status = falcon.HTTP_201

        except  requests.exceptions.HTTPError as e:
            print(e)
            resp.body = "error : " + str(e)















    def cyphergraph(self, lbl="", ref=""):
        # SEARCH QUERY
        session = driver.session()
        if ref == "":
            qry1 = 'MATCH (a:{})  RETURN a.title AS name, a.ref AS reg, a.desc as desc'.format(lbl.upper())
        else:
            qry1 = 'MATCH (a:{}) where a.ref="{}" RETURN a.title AS name, a.ref AS reg, a.desc as desc'.format(
                lbl.upper(), ref)

        print("Qry = {}".format(qry1))
        result = session.run(qry1)

        self.listr = ["Hello", "World"]
        self.listr.append(lbl)
        self.listr.append(ref)
        for record in result:
            print("{}  :  {} : {}".format(record["name"], record["reg"], record["desc"]))
            self.listr.append([record["name"], record["reg"], record["desc"]])
        session.close()
        return self.listr


    def postgraph(self, dataPack="", lbl=""):

        session = driver.session()

        dada = dataPack
        datameta = {'created_by': 'Spanarchian', 'created_on': 'CodeNode'}

        with session.begin_transaction() as tx:
            qry = "MERGE (s :STATUS:CREATED) CREATE (p :"+dada["payload"]["lbl"]+") SET p={payload} \
            MERGE (s)<-[r :CURRENT_STATUS]-(p) set r={meta}\
            set s={metadata}return s"

            print ("QRY = {}".format(qry))
            tx.run(qry, {"payload": dada["payload"], "meta": dada["metadata"], 'metadata': datameta})
            tx.success = True
        session.close()
