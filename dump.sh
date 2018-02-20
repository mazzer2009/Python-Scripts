#!/bin/bash
i=0
while true
do
	sudo tcpdump -i enp0s31f6  -w  myfile_$i & 
	pid=$!
	sleep 30
	kill $pid
	i=$(($i+1))
	echo $pid
done

