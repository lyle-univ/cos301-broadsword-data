#!/bin/bash

#start the server
#Web console can be seen at localhost:8081
./flink-1.2.0/bin/start-local.sh 
#start the data stream on port 2000
python cos301-broadsword-data/src/location_generator.py & echo $! > generator.pid
genpid=$(cat generator.pid)
#read from the data stream using flink
flink-1.2.0/bin/flink run -c LocationStreaming.StreamingJob cos301-broadsword-data/location-streaming/target/location-streaming-0.1.jar
#kill the data stream
kill -9 $genpid
