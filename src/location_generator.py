#!/usr/bin/python

from random import randint

def gen_random_longitude():
  deg = randint(-180,180)
  min = randint(0,60)
  sec = randint(0,60)
  subsec = randint(0,9)
  return str(deg)+str(min)+str(sec)+str(subsec)

