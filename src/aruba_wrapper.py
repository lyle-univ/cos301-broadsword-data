import urllib2

class Aruba:

    def __init__(self, host_name, port, username, password):
        self.host_name = host_name
        self.port = port
        self.username
        self.password

    "TODO: add exception handling"
    def get(self,query_string):
        p = urllib2.HTTPPasswordMgrWithDefaultRealm()
        p.add_password(None, self.host_name+":"+self.port+"/"+query_string, self.username, self.password)
        handler = urllib2.HTTPBasicAuthHandler(p)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)
        return urllib2.urlopen(url).read()
