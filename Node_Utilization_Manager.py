#!/usr/bin/python
#
#	Node_Utilization_Manager.py
#		11/14/12
#	Daemon that uses a utilization schedule to control the CPU utilization
#		of servers inside of BlueCenter
#
#	author: Joshua Ferguson
#		jwfergus@asu.edu | joshuawferguson@gmail.com	


import csv	# Read CSV files
import os	# Lets us issue bash commands
import sys	# Get command line arguments
from datetime import datetime	# Naturally, lets us get the current time
import time
import subprocess


def start_processes(number_of_processes, command_args):
	process_list = list()
	for i in range(number_of_processes):
		process_list.append(subprocess.Popen(command_args))
	return process_list

def start_cpu_limit(util_procs, limit):
	cpu_limit_procs = list()
	for process in util_procs:
		cpu_limit_args = ['/usr/bin/cpulimit',  '-p',  str(process.pid),  '-l',  str(limit)]
		cpu_limit_procs.append(subprocess.Popen(cpu_limit_args))
	return cpu_limit_procs

def kill_processes(process_list):
	for process in process_list:
		os.system("kill -9 " + str(process.pid))

def main():

	for process in cpu_limit_procs:
		print "cpulimit process: " + str(process.pid) + " started."
	time.sleep(6)
	kill_processes(cpu_limit_procs)
	print "cpulimit processes killed"
	time.sleep(6)


def test():

		# Need to switch from 'with' to try/except at some point
	with open(sys.argv[1], 'rb') as schedule_file:
		schedule_reader = csv.reader(schedule_file)
		
		#
		# Start our utilization processes and store them in util_procs
		#		
		cwd = os.getcwd()
		util_args = [(cwd+'/util')]
		util_procs = start_processes(4, util_args)

		#
		# Start the initial cpu_limit processes at 100 limit
		#
		current_cpu_limit_procs = start_cpu_limit(util_procs, 100) 
		while True:
			current_time = int(datetime.now().strftime('%s'))
			current_row = schedule_reader.next()
			sleep_time_diff = (int(current_row[1]) - current_time)

			#
			#	Set Utilization
			#
			new_cpu_limit_procs = start_cpu_limit(util_procs,int(current_row[2]))
			kill_processes(current_cpu_limit_procs)
			current_cpu_limit_procs = new_cpu_limit_procs 

			#
			#	Sleep until next time window
			#
			print "Current Time Window: " + str(current_row) + "; sleep time: " + str(sleep_time_diff)
			time.sleep(sleep_time_diff)
			


if __name__ == "__main__":
#	main()
	test()
