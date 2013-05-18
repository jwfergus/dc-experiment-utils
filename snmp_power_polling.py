#!/usr/bin/python

##################
# Python Script
# v1.0
# author: Joshua Ferguson <joshuawferguson@gmail.com>
#
# Script to automate SNMP polling of inlet and outlet power measurments on CDU's in Impact Lab's BlueCenter.
#
# Parameters:
#  1: number of iterations (minutes) to run
##################


import subprocess
import sys
import time
import datetime

#
#	Defined functions section
###############################################

#
#	poll does a single sweep of polling all outlets on a single CDU
#		first it appends the current time to the output file 
#		then it appends the results of each SNMP request to the output file
#		

def poll(file_handle):
	file_handle.write(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S') + "\n")
	outlets = range(1, 9)
	branches = range(1, 4)

	for branch in branches:

		#
		# Poll outlets
		#
		for outlet in outlets:
			raw_snmp_output = subprocess.check_output(["snmpget", "-v2c", "-c", "public", "192.168.2.40", "iso.3.6.1.4.1.1718.3.2.3.1.14.1." + str(branch) + "." + str(outlet)])
			file_handle.write(str(branch) + "," + str(outlet) + "," + str(raw_snmp_output.split()[3]) + "\n")
		
		#
		# Poll inlets
		#
		raw_snmp_output = subprocess.check_output(["snmpget", "-v2c", "-c", "public", "192.168.2.40", "iso.3.6.1.4.1.1718.3.2.2.1.12.1." + str(branch)])
		file_handle.write(str(branch) + "," + str(raw_snmp_output.split()[3]) + "\n")


#
#	Main execution section
###############################################

#
#	Prompt user for results file
#

filename = raw_input("Enter a filename for this experiment's output:")

#
#	For the number of iterations (minutes) the caller supplies, iterate, call poll() and sleep
#
for minute in range(int(sys.argv[1])):
	with open(filename, "a") as output_file:
		poll(output_file)
	time.sleep(60)	
