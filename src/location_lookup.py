import json
import aruba_wrapper

class LocationLookup:
	def __init__(self, hostname, port, username, password):
		self.aruba_handle = aruba_wrapper.Aruba(hostname,port,username,password)
 
	def get_json(self,mac_addr):
		raw_json = self.aruba_handle.get('/api/v1/location?sta_eth_mac='+mac_addr)
		return json.loads(raw_json)


	def lookup(self,mac_addrress):
		obj = self.get_json(mac_addrress)
		for field in obj['Location_result']:
			if 'msg' in field:
				return ("{\"x\": "+str(field['msg']['sta_location_x'])+", \"y\": "+str(field['msg']['sta_location_y'])+", \"building_id\": \""+field['msg']['building_id']+"\", \"floor_id\": \""+field['msg']['floor_id']+"\"}")
		                
		        	
