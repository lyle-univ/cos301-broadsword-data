import urllib2

class Aruba:

    def __init__(self, host_name, port, username, password):
        self.host_name = host_name
        self.port = port
        self.username=username
        self.password=password

    "TODO: add exception handling"
    def get(self,query_string):
        raw_json = open(query_string, 'r').read()
		return json.loads(raw_json)
        
