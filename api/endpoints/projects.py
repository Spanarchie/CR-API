class MainHandler3:
    """docstring for MainHandler"""
    def on_get(self, req, resp):
        import requests
        try:
            data = "Hello Welcome to Docker -> PROJECTS -> Falcon"
            resp.body = data
        except  requests.exceptions.HTTPError as e:
            print (e)
            resp.body = "error : " + str(e)