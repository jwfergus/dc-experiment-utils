#!/bin/bash
# Linux/UNIX box with ssh key based login
# SSH User name
USR="root"
 # connect each host and give command
for host in $(cat hostname.txt); 
do
#ssh $USR@$host 'bash -s' < dir.sh
scp $USR@$host:/home/tmprt1/temp1.out /home/bluetool/Desktop/moni/temp_$host.txt
done

