#!/usr/bin/python

import socket
from random import randint

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

HOST = ''
PORT = 2000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
#from here: http://stackoverflow.com/questions/4465959/python-errno-98-address-already-in-use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
s.bind((HOST, PORT))
s.listen(4);


