#!/usr/bin/python

import socket
from random import randint
from socket import error as SocketError
import errno

def gen_random_longitude():
  deg = randint(-180,180)
  min = randint(0,60)
  sec = randint(0,60)
  subsec = randint(0,9)
  return str(deg)+"."+str(min)

def gen_random_latitude():
  deg = randint(0,90)
  min = randint(0,60)
  sec = randint(0,60)
  subsec = randint(0,9)
  return str(deg)+"."+str(min)

def gen_random_altitude():
  return str(randint(0,4000))

HOST = ''
PORT = 2000
COUNT = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
#from here: http://stackoverflow.com/questions/4465959/python-errno-98-address-already-in-use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
s.bind((HOST, PORT))
s.listen(4);

while True:
  try:
      sock,addr = s.accept()
      send = 1
      while send!=0: 
          send = sock.send('{"longitude":'+gen_random_longitude()+',"latitude":'+gen_random_latitude()+',"altitude":'+gen_random_altitude()+',"ID":'+str(randint(0,999999999))+',"MACAddr":"34-32-34-3q-4c"}\n')
        
  except SocketError as e:
    continue #do nothing
  finally:
      sock.close();
     