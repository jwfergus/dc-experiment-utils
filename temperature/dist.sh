#!/bin/bash
# Linux/UNIX box with ssh key based login
# SSH User name
USR="root"
 # connect each host and give command
for host in $(cat hostname.txt); 
do
ssh $USR@$host 'bash -s' < dir.sh
scp /home/bluetool/Desktop/moni/sctemp.sh $USR@$host:/home/tmprt1/
done
