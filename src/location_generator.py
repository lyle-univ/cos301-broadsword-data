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
  return str(deg)+str(min)+str(sec)+str(subsec)

def gen_random_latitude():
  deg = randint(0,90)
  min = randint(0,60)
  sec = randint(0,60)
  subsec = randint(0,9)
  return str(deg)+str(min)+str(sec)+str(subsec)

def gen_random_altitude():
  return str(randint(0,4000))

def gen_wrong_longitude():
  deg = randint(0,1000)
  min = randint(60,100)
  sec = randint(60,100)
  subsec = randint(0,100)
  return str(deg)+str(min)+str(sec)+str(subsec)

def gen_wrong_latitude():
  deg = randint(0,900)
  min = randint(60,100)
  sec = randint(60,100)
  subsec = randint(0,100)
  return str(deg)+str(min)+str(sec)+str(subsec)

HOST = ''
PORT = 3000
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
        if COUNT%5 == 0 : 
          send = sock.send('{"longitude":'+gen_wrong_longitude()+',"latitude:"'+gen_wrong_latitude()+',"altitude":'+gen_random_altitude()+',"ID:"'+str(randint(0,999999999))+'}\n')

        else : 
          send = sock.send('{"longitude":'+gen_random_longitude()+',"latitude:"'+gen_random_latitude()+',"altitude":'+gen_random_altitude()+',"ID:"'+str(randint(0,999999999))+'}\n')

        COUNT = COUNT+1
        
  except SocketError as e:
    continue #do nothing
  finally:
    sock.close();

