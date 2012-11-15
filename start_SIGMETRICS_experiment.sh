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
set filename [lindex $argv 1]
set timeout 5
# spawn the scp thread
spawn scp $filename bluetool@$input_ip:/home/bluetool/


# When prompted for a password, give it (MUST BE SET AT THE TOP OF THE FILE)
expect "?" 
send "yes\r"
expect "password:" 
send "$pass\r" 
expect "$ "
send "cd mutual-exclusion-logic\r" 
expect "$ "
send "sudo -k\r"
expect "$ "
send "make\r"
expect "$ "
send "sudo su\r"
expect "mel:"
send "$pass\r" 
expect "# "
send "nohup python node_main.py &\r"
expect "'"
