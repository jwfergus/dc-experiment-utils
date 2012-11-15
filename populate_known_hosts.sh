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
expect "?" 
send "yes\r"
expect "password:" 
send "$pass\r" 
expect "$ "
