#! /bin/bash

clear

echo "***START***"

echo "What Wireless Interface in Monitor Mode (i.e. wlan0mon): "
read interface

airdump-ng $interface

echo "***DONE***"

exit 0
