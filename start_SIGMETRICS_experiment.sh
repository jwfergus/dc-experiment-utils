#!/usr/bin/expect -f

##################
# Expect Script
# v0.1
# author: Joshua Ferguson <jwfergus@asu.edu>
# 
# Script for moving arbitrary files with a timeout
##################



# IMPORTANT VARIABLE, WILL NOT WORK WITHOUT CHANGE
set pass "bluetool"

# Get IP address as input
set input_ip [lindex $argv 0]
set timeout 5
# spawn the scp thread
spawn ssh bluetool@$input_ip


# When prompted for a password, give it (MUST BE SET AT THE TOP OF THE FILE)
expect "password:" 
send "$pass\r" 
expect "$ "
send "mv Chassis* chassis.schedule\r"
expect "$ "
send "gcc -o util utilization.c -lpthread\r"
expect "$ "
send "sudo -k\r"
expect "$ "
send "sudo su\r"
expect "bluetool:"
send "$pass\r" 
expect "# "
send "chmod +x util\r"
expect "# "
send "nohup python Node_Utilization_Manager.py chassis.schedule &\r"
expect "'"
