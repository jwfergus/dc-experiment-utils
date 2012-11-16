#!/bin/bash
# Linux/UNIX box with ssh key based login
# SSH User name
USR="root"
 # connect each host and give command
for host in $(cat hostname.txt); 
do
nohup ssh $USR@$host 'bash -s' < com.sh &
done
