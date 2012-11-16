Distrubuted utilization script for BlueCenter

Framework that takes a file representing a utilization and on/off schedule for the bluecenter and runs the servers at such a schedule.

This framework should be paired with daemons to read temperature (via IPMITools) and power usage (via SNMP from the Server Power Manager [SPM]) in the datacenter.

The major functions of these scripts are:

1)Given a data center utilization schedule (provided by Zahra), create and distribute individual schedules to each server.
2)Distribute (or update) the latest script to:
	-read and execute the schedule to each server
	-collect temperature measurements
	-Issue commands (to all servers) to start the utilization/schedule daemon and begin collecting temperature

How to perform these functions, in detail:

1)To create individual schedules you must take a schedule provided by Zahra (such as the one attached), of the form:
	-Column indices are chassis numbers
	-Row indices are time windows
	-Cell values are utilization values
2)Given such a schedule, transpose it and convert it to comma separated values, rather then space separated. (No script to do this yet, but it can be done easily in matlab).
3)With the now CSV, transposed, schedule run the script Node_Schedule_Generator.py as such:
	-user@host$ python Node_Schedule_Generator.py <CSV_transposed_schedule> <start_time_of_experiment_in_UNIX_seconds>
	-A good server for getting the unix time you'd like to start the experiment at is: http://troink.net/unix-time-converter
4)Now you must distribute this schedule along with the script to utilize the servers according to that schedule:
	-user@host$ python Send_Schedules.py
5)Once the schedules and utilization scripts have been distributed, you can start the utilization daemon:
	-user@host$ python Start_Utilization_Daemons.py
	-Note: this file was mysteriously deleted from the bootserver and no backup exists. It is almost a verbatim copy of Send_Schedules.py, however, so it should take ~20 mins to remake and test. 
