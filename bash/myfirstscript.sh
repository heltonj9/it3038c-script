#!/bin/bash
# This script outputs the IP address and Hostname of a machine

greeting="kachow"
echo $greeting, thanks for joining me
echo '$greeting, thanks for joining us! You owe me $20'
echo "$greeting, thanks for joining us!"
echo "$greeting, you owe me $20"

echo Machine Type: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working Dir: $PWD
echo Home Dir: $HOME
echo Session Length: $SECONDS
