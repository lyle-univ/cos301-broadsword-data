#!/bin/bash

nohup ./nsqlookupd &
nohup ./nsqd --lookupd-tcp-address=127.0.0.1:4160 &
nohup ./nsqadmin --lookupd-http-address=127.0.0.1:4161 &
