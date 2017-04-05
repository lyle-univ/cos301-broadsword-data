import nsq
import json

address_port = 'http://127.0.0.1:4161'

def publish(src, dest, msgtype, content):
  print src
  print dest
  print msgtype
  print content

def Searcher(mac):
  return mac

def handler(message):
  obj = json.loads(message.body)
  if (obj['dest'] == 'Data' and obj['msgType'] == 'request'):
#    print obj['content']['mac']
    location = Searcher(obj['content']['mac'])
    src = obj['dest']
    dest = obj['src']
    msgtype = "response"
    content = location
    publish(src, dest, msgtype, content)
    return True

r = nsq.Reader(message_handler=handler, lookupd_http_addresses=[address_port],
                topic='Data', channel='navup', lookupd_poll_interval=15)
nsq.run()
