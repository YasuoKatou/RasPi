#!/bin/bash

PID_FILE=/home/pi/usbHDD/music/player.pid

if [ -f $PID_FILE ]; then
	echo "kill player"
	pid=$(<$PID_FILE)
	echo $pid
	kill -SIGINT $pid
else
	echo "stopped player"
fi
