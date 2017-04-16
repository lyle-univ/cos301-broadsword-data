import nsq
import json
import tornado.ioloop

address_port = 'http://127.0.0.1:4161'
writer = nsq.Writer(['127.0.0.1:4150'])

def publish(src, dest, msgtype, content):
  result="{\"src\":\""+src+"\",\"dest\":\""+dest+"\",\"msgType\":\""+msgtype+"\",,\"queryType\":\"getCurrentLocation\",\"content\":\""+content+"\"} }"
  return result
  
def Searcher(mac_string):
  file = open("output.txt", "r")
  lines = file.readlines()
  for line in lines:
    if mac_string in line:
      parsed_json = json.loads(line)
      mac=parsed_json["MacAddress"]
      longitude=parsed_json["longitude"]
      latitude=parsed_json["latitude"]
      x=parsed_json["x"]
      y=parsed_json["y"]
      result=("{\"MacAddress\":\""+mac+"\",\"Longitude\":\""+longitude+"\",\"Latitude\":\""+latitude+"\",\"x\":\""+x+"\",\"y\":\""+y+"\"}")
      return result
  file.close()
m="";
def handler(message):
  obj = json.loads(message.body)
  if (obj['src'] == 'gis' and obj['msgType'] == 'request'):
#    print obj['content']['mac']
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