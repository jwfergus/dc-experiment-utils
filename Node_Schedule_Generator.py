#!/usr/bin/python
#
#	Node_Schedule_Generator.py
#		11/14/12
#	Script to take a start time, matrix of server utilizations and generate
#		BlueCenter utilization schedules for each node
#	
#	author: Joshua Ferguson
#		jwfergus@asu.edu | joshuawferguson@gmail.com	

import csv	# Read CSV files
import sys	# Get command line arguments

def generate_chassis_schedules(main_schedule, start_time):

	with open(main_schedule, 'rb') as schedule_file:
		schedule_reader = csv.reader(schedule_file)
		count = 1
		while True:
			current_line = schedule_reader.next()			
			with open (("Chassis-" + str(count) + ".schedule"),'wb') as chassis_schedule_file:
				current_util_time = int(start_time)
				for util_values in current_line:
					rounded_util = util_values.split('.')[0]
					if len(util_values.split('.')) > 1 and util_values.split('.')[0] == '0':
						rounded_util = '1'
					chassis_schedule_file.write(str(current_util_time) + "," + str(current_util_time+10) + "," + rounded_util + "\n")
					current_util_time = current_util_time + 10
			count = count + 1


if __name__ == "__main__":
	generate_chassis_schedules(sys.argv[1], sys.argv[2])
