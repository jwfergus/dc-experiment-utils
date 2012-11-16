#!/bin/bash
slp=$1
len=$2
c=1
while [ $c -le $len ]
do
	ipmitool sdr | grep "Ambient Temp\|CPU [0-9] Temp" | awk '{print $1 " " $2 " " $3 " " $4 " " $5 " " $6}' | sed "s/^/$(date) /" >> /home/tmprt1/temp1.out
	(( c++ ))
        sleep $slp
done
