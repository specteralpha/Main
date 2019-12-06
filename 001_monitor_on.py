#! /bin/bash

clear

echo "***START***"

echo "What Wireless Interface (i.e. wlan0): "
read interface

sudo ifconfig $interface down

sudo airmon-ng check kill

sudo ifconfig $interface up

sudo airmon-ng start $interface

echo "***DONE***"

exit 0