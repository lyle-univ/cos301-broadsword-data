import urllib2

class Aruba:
    host_name = ""
    port = ""

    def __init__(self, host_name, port):
        self.host_name = host_name
        self.port = port

    "TODO: add exception handling"
    def get(self,query_string):
        return urllib2.urlopen(self.host_name+":"+self.port+"/"+query_string).read()
