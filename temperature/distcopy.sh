#!/bin/bash
# Linux/UNIX box with ssh key based login
# SSH User name
USR="root"
 # connect each host and give command
for host in $(cat hostname.txt); 
do
	echo -n $host: `ssh -o ConnectTimeout=5 $USR@$host 'date'`
	echo " - " `date`
done
