import falcon
import requests
import json
import logging
import os
from endpoints import reactors

class MainHandler:
    """docstring for MainHandler"""
    def on_get(self, req, resp):
        try:
            data = "Hello Welcome to Docker -> Nginx -> Gunicorn -> Falcon"
            resp.body = data
        except  requests.exceptions.HTTPError as e:
            print (e)
            resp.body = "error : " + str(e)

class MainHandler2:
    """docstring for MainHandler"""
    def on_get(self, req, resp):
        try:
            data = "Hello Welcome to Docker -> stuff -> Falcon"
            resp.body = data
        except  requests.exceptions.HTTPError as e:
            print (e)
            resp.body = "error : " + str(e)

reactr = reactors.MainHandler3()


api = falcon.API()
api.add_route('/', MainHandler())
api.add_route('/stuff', MainHandler2())
api.add_route('/rubish', reactr)



