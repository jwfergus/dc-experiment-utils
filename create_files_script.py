import os
file_size = 1024

while(file_size < 10490000):
	os.system('dd if=/dev/zero of=upload_test_' + str(file_size) + ' bs=' + str(file_size) + ' count=1')
	file_size = file_size * 2

