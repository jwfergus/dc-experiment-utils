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

def test_script(node_schedule, start_time):

	with open(node_schedule, 'rb') as schedule_file:
		with open ((node_schedule[:-8] + "instance"),'wb') as instance_file:

			schedule_reader = csv.reader(schedule_file)
			schedule_reader.next() # Move past the first line of file (just a comment)
			while True:
				current_row = schedule_reader.next()
				instance_file.write( str(int(current_row[0]) + int(start_time)) + "," + str(int(current_row[1]) + int(start_time)) + "," + current_row[2] + "\n")


if __name__ == "__main__":
	test_script(sys.argv[1], sys.argv[2])
