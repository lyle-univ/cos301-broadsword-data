import urllib2
import json

class FloorLookup:
     def __init__(self, hostname, port, username, password):
         self.aruba_handle = aruba_wrapper.Aruba(hostname,port,username,password)

    def get_json(self):
        raw_json = aruba_handle.get("/api/v1/floor")
        return json.loads(raw_json)

    def lookup(self,building_id,floor_id):
        obj = self.get_json()
        for field in obj['Floor_result']:
                if 'msg' in field:
                    if building_id in field['msg']['building_id']:
                            if floor_id in field['msg']['floor_id']:
                                return field['msg']['floor_name']
                        
                #return "Error:Cannot locate floor "
