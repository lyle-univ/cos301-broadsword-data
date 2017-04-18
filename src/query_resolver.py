import nsq
import json
import tornado.ioloop
import building_lookup
import floor_lookup
import location_lookup
import json

address_port = 'http://127.0.0.1:4161'
writer = nsq.Writer(['127.0.0.1:4150'])

def publish(src, dest, msgtype, content):
  result="{\"src\":\""+src+"\",\"dest\":\""+dest+"\",\"msgType\":\""+msgtype+"\",,\"queryType\":\"getCurrentLocation\",\"content\":\""+content+"\"} }"
  return result
  
def Searcher(mac_string):
  locationL= location_lookup.LocationLookup()
  location_json=json.loads(locationL.lookup(mac_string))
  buildingID=location_json['building_id']
  floorID=location_json['floor_id']
  x=location_json['x']
  y=location_json['y']

  
  floorL=floor_lookup.FloorLookup()
  floor_name=floorL.lookup(buildingID,floorID)

  buildingL= building_lookup.BuildingLookup()
  building_name=buildingL.lookup(buildingID)

  final_content=("{ \"mac_address\": \""+mac_string+"\" ,\"x\": "+str(x)+", \"y\": "+str(y)+", \"building_name\": \""+building_name+"\", \"floor_name\": \""+floor_name+"\"}")
  return final_content

m="";
def handler(message):
  obj = json.loads(message.body)
  if (obj['src'] == 'gis' and obj['msgType'] == 'request'):
    #print obj['content']['mac']
    location = Searcher(obj['content']['mac'])
    src = obj['src']
    dest = obj['dest']
    msgtype = "response"
    content = location
    m=publish(src, dest, msgtype, content)
    tornado.ioloop.PeriodicCallback(pub_message(m), 1000).start()
    return True
def pub_message(message):
  writer.pub('navigation',str(message), finish_pub)
def finish_pub(conn, data):
  print(data)
  #tornado.ioloop.IOLoop.current().stop()''



r = nsq.Reader(message_handler=handler, lookupd_http_addresses=[address_port],
                topic='gis', channel='navup', lookupd_poll_interval=15)
nsq.run()
