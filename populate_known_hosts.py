#!/usr/bin/python
#
#	Send_Schedules.py
#		11/14/12
#	Script to deliver schedules that are labeled by chassis to the
#		individual servers.
#
#	**********
#	* !STILL NEED TO ELIMINATE UNUSED SERVERS!
#	*****************************
#
#	author: Joshua Ferguson
#		jwfergus@asu.edu | joshuawferguson@gmail.com	
import math
import os

def generate_server_chassis_map():
	server_chassis_map = list()
	chassis_counter = 12 #Strange value for a reason, look at how it's used
	for rack in range(1,9):
		for server_id in range(1,37):
			server_chassis_map.append((("192.168."+ str(rack) + "." + str(server_id)),str(int(math.floor(chassis_counter/12)))))
			chassis_counter +=1


	for server in server_chassis_map:
		if((" " + server[0].split(".")[3] + " ") in " 1 2 3 4 5 6 13 14 15 16 17 18 25 26 27 28 29 30 "):
			continue
		os.system("./move_file Chassis-" + server[1] + ".schedule "+ server[0])
		os.system("./move_file utilization.c "+ server[0])
		os.system("./move_file Node_Utilization_Manager "+ server[0])


if __name__ == "__main__":
	generate_server_chassis_map()
