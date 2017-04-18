import urllib2
import json

class LocationLookup:
 
 
	def get_json(self,mac_addr):
		url = ('https://137.215.6.208/api/v1/location?sta_eth_mac='+mac_addr)
 		username = ''
		password = ''
		p = urllib2.HTTPPasswordMgrWithDefaultRealm()
		p.add_password(None, url, username, password)
		handler = urllib2.HTTPBasicAuthHandler(p)
		opener = urllib2.build_opener(handler)
		urllib2.install_opener(opener)
		page = urllib2.urlopen(url).read()
        	return json.loads(page)

	def lookup(self,mac_addrress):
	    obj = self.get_json(mac_addrress)
	    for field in obj['Location_result']:
		    	if 'msg' in field:
		        	return ("{\"x\": "+str(field['msg']['sta_location_x'])+", \"y\": "+str(field['msg']['sta_location_y'])+", \"building_id\": \""+field['msg']['building_id']+"\", \"floor_id\": \""+field['msg']['floor_id']+"\"}")
		                
		        	
