import urllib2
import json

class FloorLookup:
    # def __init__(self, hostname, port):
    #     self.aruba_handle = aruba_wrapper.Aruba(hostname,port)
    def get_json(self):
        url = 'https://137.215.6.208/api/v1/floor'
        username = 'admin'
        password = 'Aruba123!'
        p = urllib2.HTTPPasswordMgrWithDefaultRealm()
        p.add_password(None, url, username, password)
        handler = urllib2.HTTPBasicAuthHandler(p)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)
        page = urllib2.urlopen(url).read()
        return json.loads(page)

    def lookup(self,building_id,floor_id):
        obj = self.get_json()
        for field in obj['Floor_result']:
                if 'msg' in field:
                    if building_id in field['msg']['building_id']:
                            if floor_id in field['msg']['floor_id']:
                                return field['msg']['floor_name']
                        
                #return "Error:Cannot locate floor "