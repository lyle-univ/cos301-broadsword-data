#!/usr/bin/python

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

