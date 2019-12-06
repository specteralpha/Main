#! /bin/bash

clear

echo "***START***"

echo "What Wireless Interface in Monitor Mode (i.e. wlan0mon): "
read interface

echo "What MAC Address: "
read address

echo "What Channel: "
read channel

echo "Save name?: "
read save

if [ $save > 0 ]
then
	airodump-ng --bssid $address --channel $channel --write $save $interface
else
	airodump-ng --bssid $address --channel $channel $interface
fi

echo "***DONE***"

exit 0
